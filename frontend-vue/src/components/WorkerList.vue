<template>
  <ul class="space-y-2">
    <!-- WORKER ITEM -->
    <li
      v-for="w in store.workers"
      :key="w.id"
      class="p-3 border border-gray-300 rounded-lg flex items-center justify-between"
    >
      <div class="flex items-center gap-3">
        <input
          v-if="editingId === w.id"
          v-model="editName"
          class="border px-2 py-1 rounded"
        />

        <span v-else class="text-gray-800">
          {{ w.name }}
        </span>
      </div>

      <div class="flex gap-2">
        <!-- EDIT / SAVE -->
        <button
          v-if="editingId !== w.id"
          @click="startEdit(w)"
          class="px-2 py-1 bg-blue-600 text-white text-sm rounded"
        >
          Edit
        </button>

        <button
          v-else
          @click="saveEdit(w.id)"
          class="px-2 py-1 bg-green-600 text-white text-sm rounded"
        >
          Save
        </button>

        <!-- CANCEL -->
        <button
          v-if="editingId === w.id"
          @click="cancelEdit"
          class="px-2 py-1 bg-gray-500 text-white text-sm rounded"
        >
          Cancel
        </button>

        <!-- DELETE -->
        <button
          @click="remove(w.id)"
          class="px-2 py-1 bg-red-600 text-white text-sm rounded"
        >
          Delete
        </button>
      </div>
    </li>
  </ul>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useWorkersStore } from "../stores/workers";
import { useToastStore } from "../stores/toast";
const toast = useToastStore();

const store = useWorkersStore();

// Editing state
const editingId = ref<number | null>(null);
const editName = ref("");

const startEdit = (worker: any) => {
  editingId.value = worker.id;
  editName.value = worker.name;
};

const cancelEdit = () => {
  editingId.value = null;
  editName.value = "";
};

const saveEdit = async (id: number) => {
  await store.updateWorker(id, editName.value);
  toast.show("Worker updated!", "success");
  cancelEdit();
};

const remove = async (id: number) => {
  if (!confirm("Delete worker?")) return;
  toast.show("Worker deleted!", "success");
  await store.deleteWorker(id);
};
</script>
