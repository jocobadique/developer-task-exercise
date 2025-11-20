<template>
  <div class="border p-8 border-gray-300 rounded-lg space-y-4 mb-4">
    <h3 class="text-lg font-semibold">Add Shift</h3>

    <!-- Worker dropdown -->
    <div class="flex flex-col gap-1">
      <label class="font-medium">Worker</label>
      <select
        v-model="workerId"
        class="border border-gray-300 px-3 py-2 rounded-lg"
      >
        <option disabled value="">Select worker</option>
        <option v-for="w in workersStore.workers" :key="w.id" :value="w.id">
          {{ w.name }}
        </option>
      </select>
    </div>

    <!-- Start datetime -->
    <div class="flex flex-col gap-1">
      <label class="font-medium">Start</label>
      <VueDatePicker
        v-model="start"
        :enable-time="true"
        :is-24="true"
        input-class="border px-3 py-2 rounded w-full"
      />
    </div>

    <!-- End datetime -->
    <div class="flex flex-col gap-1">
      <label class="font-medium">End</label>
      <VueDatePicker
        v-model="end"
        :enable-time="true"
        :is-24="true"
        input-class="border px-3 py-2 rounded w-full"
      />
    </div>

    <!-- Error -->
    <p v-if="error" class="text-red-600 text-sm">
      {{ error }}
    </p>

    <!-- Submit -->
    <button
      @click="submit"
      class="bg-purple-600 hover:bg-purple-700 text-white px-4 py-2 rounded"
    >
      Create Shift
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { VueDatePicker } from "@vuepic/vue-datepicker";
import { useToastStore } from "../stores/toast";
import { useWorkersStore } from "../stores/workers";
import { useShiftsStore } from "../stores/shifts";

const workersStore = useWorkersStore();
const shiftsStore = useShiftsStore();
const toast = useToastStore();

// Form state
const workerId = ref<number | "">("");
const start = ref<Date | null>(null);
const end = ref<Date | null>(null);
const error = ref("");

const submit = async () => {
  error.value = "";

  if (!workerId.value || !start.value || !end.value) {
    error.value = "Please fill all fields.";
    return;
  }

  try {
    const iso = (d: Date) => d.toISOString();

    await shiftsStore.addShift(
      Number(workerId.value),
      iso(start.value),
      iso(end.value)
    );

    // refresh shifts
    await shiftsStore.fetchShifts();

    // reset form
    workerId.value = "";
    start.value = null;
    end.value = null;
    toast.show("Shift created!", "success");
  } catch (err: any) {
    toast.show(err.response?.data?.error || "Unable to create shift.", "error");
    error.value = err.response?.data?.error || "Unable to create shift.";
  }
};
</script>
