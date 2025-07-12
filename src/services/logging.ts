class Logger {
  debug(message: string, data?: any) {
    console.debug(`[DEBUG] ${message}`, data);
  }

  info(message: string, data?: any) {
    console.info(`[INFO] ${message}`, data);
  }

  warn(message: string, data?: any) {
    console.warn(`[WARN] ${message}`, data);
  }

  error(message: string, data?: any) {
    console.error(`[ERROR] ${message}`, data);
  }
}

const logger = new Logger();

export default logger;
