import { defineStore } from "pinia";
import { api } from "../api/api";

export const useWorkersStore = defineStore("workers", {
  state: () => ({
    workers: [] as any[],
    loading: false,
  }),

  actions: {
    async fetchWorkers() {
      this.loading = true;
      const res = await api.get("/workers/");
      this.workers = res.data;
      this.loading = false;
    },

    async addWorker(name: string) {
      await api.post("/workers/", { name });
      await this.fetchWorkers();
    },

    async updateWorker(id: number, name: string) {
      await api.put(`/workers/${id}/`, { name });
      await this.fetchWorkers();
    },

    async deleteWorker(id: number) {
      await api.delete(`/workers/${id}/`);
      await this.fetchWorkers();
    },
  },
});
