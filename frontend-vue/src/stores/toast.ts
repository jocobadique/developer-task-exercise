import { defineStore } from "pinia";

export const useToastStore = defineStore("toast", {
  state: () => ({
    message: "",
    type: "success" as "success" | "error",
    visible: false,
  }),

  actions: {
    show(message: string, type: "success" | "error" = "success") {
      this.message = message;
      this.type = type;
      this.visible = true;

      // auto-hide after 3 seconds
      setTimeout(() => {
        this.visible = false;
      }, 3000);
    },
  },
});
