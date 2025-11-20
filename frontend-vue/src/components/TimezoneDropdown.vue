<template>
  <div class="relative">
    <input
      v-model="query"
      @focus="open = true"
      @input="open = true"
      placeholder="Search timezone..."
      class="border border-gray-300 rounded-lg w-full px-3 py-2"
    />

    <!-- DROPDOWN LIST -->
    <div
      v-if="open"
      class="absolute z-10 w-full max-h-60 overflow-y-auto bg-white border border-gray-300 rounded shadow mt-1"
    >
      <div
        v-for="tz in filtered"
        :key="tz"
        @click="select(tz)"
        class="px-3 py-2 cursor-pointer hover:bg-gray-100"
      >
        {{ tz }}
      </div>

      <!-- NO RESULTS -->
      <div v-if="filtered.length === 0" class="px-3 py-2 text-gray-500">
        No results
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from "vue";
import { timezones } from "../data/timezones";

const model = defineModel<string>();

const open = ref(false);
const query = ref("");

// Filter timezones
const filtered = computed(() => {
  if (!query.value) return timezones;
  return timezones.filter((tz: string) =>
    tz.toLowerCase().includes(query.value.toLowerCase())
  );
});

// When user selects a timezone
const select = (tz: string) => {
  model.value = tz;
  query.value = tz;
  open.value = false;
};

// Sync with store value ONLY when closed
watch(
  () => model.value,
  (val) => {
    if (!open.value && val) {
      query.value = val;
    }
  },
  { immediate: true }
);

// Close on outside click
onMounted(() => {
  document.addEventListener("click", (e) => {
    if (!(e.target as HTMLElement).closest(".relative")) {
      open.value = false;
    }
  });
});
</script>
