<template>
  <div class="flex flex-col gap-[24px]">
    <h2 class="text-lg font-bold">Ваши заметки</h2>
    <div v-if="isLoading" class="flex flex-col gap-[16px]">
      <USkeleton class="w-full h-[240px]"></USkeleton>
      <USkeleton class="w-full h-[120px]"></USkeleton>
      <USkeleton class="w-full h-[60px]"></USkeleton>
      <USkeleton class="w-full h-[30px]"></USkeleton>
    </div>
    <ul v-else class="flex flex-col gap-[12px]">
      <li v-for="ticket in workspaceStore.tickets" :key="ticket.id">
        <Note
          :title="ticket.title"
          :description="ticket.description"
          :tags="ticket.tags"
        ></Note>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
const workspaceStore = useWorkspaceStore();
const isLoading = ref(true);

async function load() {
  isLoading.value = true;
  await workspaceStore.fetchTickets();
  isLoading.value = false;
}

load();
</script>
