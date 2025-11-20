<template>
  <transition name="fade">
    <div
      v-if="toast.visible"
      class="fixed top-4 right-4 px-4 py-2 rounded shadow text-white"
      :class="toast.type === 'success' ? 'bg-green-600' : 'bg-red-600'"
    >
      {{ toast.message }}
    </div>
  </transition>
</template>

<script setup lang="ts">
import { useToastStore } from "../stores/toast";
const toast = useToastStore();
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
