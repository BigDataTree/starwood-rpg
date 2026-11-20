#!/usr/bin/env node
// Read-only asset audit for Starwood RPG; never rewrites game or art files.
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { join } from 'node:path';

const errors = [];
const warnings = [];
const checks = [];
const check = (ok, label) => { checks.push({ ok, label }); if (!ok) errors.push(label); };
const root = process.cwd();
const source = join(root, 'index.html');
check(existsSync(source), 'index.html exists');
const html = existsSync(source) ? readFileSync(source, 'utf8') : '';
check(html.length > 1000, 'index.html is nonempty and reasonably sized');
check(/<html[\s>]/i.test(html), 'HTML root element present');
for (const name of ['V6_ACTOR_MAP', 'V6_PORTRAITS', 'actorDraw', 'buildAmbientNPCs']) {
  if (!html.includes(name)) warnings.push('Marker not found: ' + name);
}
const required = ['assets/common/actors.webp', 'assets/common/boss.webp', 'assets/portraits'];
for (const rel of required) check(existsSync(join(root, rel)), rel + ' exists');
const portraits = join(root, 'assets/portraits');
const images = existsSync(portraits) ? readdirSync(portraits).filter(f => f.toLowerCase().endsWith('.webp')) : [];
if (images.length < 73) warnings.push('Only ' + images.length + ' external portrait WebP files; embedded portraits may exist');
const files = [];
function walk(dir) {
  if (!existsSync(dir)) return;
  for (const ent of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, ent.name);
    if (ent.isDirectory()) walk(p);
    else if (ent.isFile() && ent.name.toLowerCase().endsWith('.webp')) files.push(p);
  }
}
walk(join(root, 'assets'));
for (const file of files) {
  const data = readFileSync(file);
  if (data.length < 16 || data.toString('ascii', 0, 4) !== 'RIFF' || data.toString('ascii', 8, 12) !== 'WEBP')
    errors.push('Invalid WebP header: ' + file.slice(root.length + 1));
}
const report = [
  '# Starwood RPG – scheduled static audit',
  '',
  '- Checked branch: ' + (process.env.GITHUB_AUDIT_BRANCH || 'local'),
  '- Checked revision: ' + (process.env.GITHUB_AUDIT_SHA || 'local'),
  '- Portrait WebP files: ' + images.length,
  '- Total external WebP files: ' + files.length,
  '- Result: ' + (errors.length ? 'FAIL' : 'PASS (structural only)'),
  '',
  '## Checks', ...checks.map(x => '- ' + (x.ok ? 'PASS ' : 'FAIL ') + x.label),
  '',
  '## Warnings', ...(warnings.length ? warnings.map(x => '- ' + x) : ['- None']),
  '',
  '## Errors', ...(errors.length ? errors.map(x => '- ' + x) : ['- None']),
  '',
  'This verifies presence and file headers only. It does not certify sprites, animation frames, visual quality, or gameplay.'
].join('\n');
console.log(report);
if (process.env.GITHUB_STEP_SUMMARY) {
  const { appendFileSync } = await import('node:fs');
  appendFileSync(process.env.GITHUB_STEP_SUMMARY, report + '\n');
}
if (errors.length) process.exitCode = 1;
