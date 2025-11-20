import { defineStore } from "pinia";
import { api } from "../api/api";

export const useTimezoneStore = defineStore("timezone", {
  state: () => ({
    timezone: "UTC",
    loading: false,
  }),

  actions: {
    async fetchTimezone() {
      this.loading = true;
      const res = await api.get("/timezone/");
      this.timezone = res.data.timezone;
      this.loading = false;
    },

    async updateTimezone(tz: string) {
      const res = await api.put("/timezone/", { timezone: tz });
      this.timezone = res.data.timezone;
    },
  },
});
