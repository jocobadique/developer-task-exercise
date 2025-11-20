export const timezones = (Intl as any).supportedValuesOf
  ? (Intl as any).supportedValuesOf("timeZone")
  : [];
