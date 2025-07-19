export function sanitizeForSelector(name: string) {
  return name.replace(/[^a-zA-Z0-9_-]/g, '_');
}
