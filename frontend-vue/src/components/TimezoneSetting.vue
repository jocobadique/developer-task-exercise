<template>
  <div class="p-8 space-y-3 border border-gray-300 rounded-lg">
    <h3 class="text-lg font-semibold">Preferred Timezone</h3>

    <TimezoneDropdown v-model="tz" />

    <button @click="save" class="bg-blue-600 text-white px-3 py-1 rounded">
      Save
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useTimezoneStore } from "../stores/timezone";
import TimezoneDropdown from "./TimezoneDropdown.vue";
import { useToastStore } from "../stores/toast";

const timezoneStore = useTimezoneStore();
const toast = useToastStore();

const tz = ref("");

onMounted(async () => {
  await timezoneStore.fetchTimezone();
  tz.value = timezoneStore.timezone;
});

const save = async () => {
  await timezoneStore.updateTimezone(tz.value);
  toast.show("Timezone updated!", "success");
};
</script>
