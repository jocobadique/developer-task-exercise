import { defineStore } from "pinia";
import { api } from "../api/api";

export const useShiftsStore = defineStore("shifts", {
  state: () => ({
    shifts: [] as any[],
    loading: false,
  }),

  actions: {
    async fetchShifts() {
      this.loading = true;
      const res = await api.get("/shifts/");
      this.shifts = res.data;
      this.loading = false;
    },

    async addShift(workerId: number, start: string, end: string) {
      await api.post("/shifts/", {
        worker_id: workerId,
        start,
        end,
      });
      await this.fetchShifts();
    },

    async updateShift(
      id: number,
      workerId: number,
      start: string,
      end: string
    ) {
      await api.put(`/shifts/${id}/`, {
        worker_id: workerId,
        start,
        end,
      });
      await this.fetchShifts();
    },

    async deleteShift(id: number) {
      await api.delete(`/shifts/${id}/`);
      await this.fetchShifts();
    },
  },
});
