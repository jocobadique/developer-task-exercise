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
import { ref, computed, onMounted } from "vue";
import { timezones } from "../data/timezones";

const model = defineModel<string>(); // v-model for parent

const open = ref(false);
const query = ref("");

// Filter timezones based on search query
const filtered = computed(() => {
  if (!query.value) return timezones;
  return timezones.filter((tz: any) =>
    tz.toLowerCase().includes(query.value.toLowerCase())
  );
});

// Select a timezone
const select = (tz: string) => {
  model.value = tz;
  query.value = tz;
  open.value = false;
};

// Close dropdown when clicking outside
onMounted(() => {
  document.addEventListener("click", (e) => {
    if (!(e.target as HTMLElement).closest(".relative")) {
      open.value = false;
    }
  });
});
</script>
