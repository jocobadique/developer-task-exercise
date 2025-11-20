<template>
  <div class="p-8 max-w-3xl mx-auto space-y-8">
    <TimezoneSetting />

    <section>
      <h2 class="text-xl font-semibold mb-2">Workers</h2>
      <AddWorker />
      <WorkerList />
    </section>

    <section>
      <h2 class="text-xl font-semibold mb-2">Shifts</h2>
      <AddShift />
      <ShiftList />
    </section>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useWorkersStore } from "../stores/workers";
import { useShiftsStore } from "../stores/shifts";
import AddShift from "../components/AddShift.vue";
import TimezoneSetting from "../components/TimezoneSetting.vue";
import AddWorker from "../components/AddWorker.vue";
import WorkerList from "../components/WorkerList.vue";
import ShiftList from "../components/ShiftList.vue";

const workersStore = useWorkersStore();
const shiftsStore = useShiftsStore();

onMounted(async () => {
  await workersStore.fetchWorkers();
  await shiftsStore.fetchShifts();
});
</script>
