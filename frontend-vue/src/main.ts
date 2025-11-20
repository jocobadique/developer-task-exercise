import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import "@vuepic/vue-datepicker/dist/main.css";
import { useTimezoneStore } from "./stores/timezone";

const app = createApp(App);

app.use(createPinia());

app.mount("#app");

const timezoneStore = useTimezoneStore();
timezoneStore.fetchTimezone();
