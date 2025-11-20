<template>
  <ul class="space-y-3">
    <li
      v-for="s in shiftsStore.shifts"
      :key="s.id"
      class="p-3 border border-gray-300 rounded-lg space-y-3"
    >
      <!-- EDIT VIEW -->
      <div v-if="editingId === s.id" class="space-y-2">
        <div>
          <label class="font-medium">Worker</label>
          <select
            v-model="editWorkerId"
            class="border px-2 py-1 rounded w-full"
          >
            <option disabled value="">Select worker</option>
            <option v-for="w in workersStore.workers" :key="w.id" :value="w.id">
              {{ w.name }}
            </option>
          </select>
        </div>

        <div>
          <label class="font-medium">Start</label>
          <VueDatePicker
            v-model="editStart"
            :enable-time="true"
            :is-24="true"
            input-class="border px-2 py-1 rounded w-full"
          />
        </div>

        <div>
          <label class="font-medium">End</label>
          <VueDatePicker
            v-model="editEnd"
            :enable-time="true"
            :is-24="true"
            input-class="border px-2 py-1 rounded w-full"
          />
        </div>

        <p v-if="error" class="text-red-600 text-sm">{{ error }}</p>

        <div class="flex gap-2">
          <button
            class="bg-green-600 text-white px-3 py-1 rounded"
            @click="saveShift(s.id)"
          >
            Save
          </button>
          <button
            class="bg-gray-500 text-white px-3 py-1 rounded"
            @click="cancelEdit"
          >
            Cancel
          </button>
        </div>
      </div>

      <!-- DISPLAY VIEW -->
      <div v-else class="flex items-center justify-between">
        <div>
          <p class="font-semibold">Worker: {{ s.worker_id }}</p>
          <p>{{ s.start }} → {{ s.end }}</p>
          <p class="text-sm text-gray-600">{{ s.duration_hours }} hour</p>
        </div>

        <div class="flex gap-2">
          <button
            class="bg-blue-600 text-white px-3 py-1 rounded"
            @click="startEdit(s)"
          >
            Edit
          </button>

          <button
            class="bg-red-600 text-white px-3 py-1 rounded"
            @click="remove(s.id)"
          >
            Delete
          </button>
        </div>
      </div>
    </li>
  </ul>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { VueDatePicker } from "@vuepic/vue-datepicker";
import { useToastStore } from "../stores/toast";

import { useShiftsStore } from "../stores/shifts";
import { useWorkersStore } from "../stores/workers";

const shiftsStore = useShiftsStore();
const workersStore = useWorkersStore();
const toast = useToastStore();

// Editing State
const editingId = ref<number | null>(null);
const editWorkerId = ref<number | "">("");
const editStart = ref<Date | null>(null);
const editEnd = ref<Date | null>(null);
const error = ref("");

const startEdit = (shift: any) => {
  editingId.value = shift.id;
  editWorkerId.value = shift.worker_id;
  editStart.value = new Date(shift.start);
  editEnd.value = new Date(shift.end);
};

const cancelEdit = () => {
  editingId.value = null;
  editWorkerId.value = "";
  editStart.value = null;
  editEnd.value = null;
  error.value = "";
};

const saveShift = async (id: number) => {
  if (!editWorkerId.value || !editStart.value || !editEnd.value) {
    error.value = "Please complete all fields.";
    return;
  }

  try {
    const iso = (d: Date) => d.toISOString();

    await shiftsStore.updateShift(
      id,
      Number(editWorkerId.value),
      iso(editStart.value),
      iso(editEnd.value)
    );
    toast.show("Shift updated!", "success");
    cancelEdit();
  } catch (err: any) {
    error.value = err.response?.data?.error || "Unable to update shift.";
  }
};

const remove = async (id: number) => {
  if (!confirm("Delete this shift?")) return;
  await shiftsStore.deleteShift(id);
  toast.show("Shift deleted!", "success");
};
</script>
