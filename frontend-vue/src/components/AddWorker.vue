<template>
  <div class="flex gap-3 mb-3">
    <input
      v-model="name"
      class="border border-gray-300 rounded-lg px-3 py-2"
      placeholder="Worker name"
    />
    <button @click="create" class="bg-green-600 text-white px-3 py-1 rounded">
      Add
    </button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useWorkersStore } from "../stores/workers";
import { useToastStore } from "../stores/toast";
const toast = useToastStore();
const store = useWorkersStore();
const name = ref("");

const create = async () => {
  if (!name.value.trim()) return;
  await store.addWorker(name.value);
  toast.show("Worker added!", "success");
  name.value = "";
};
</script>
