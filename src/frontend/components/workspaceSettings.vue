<script setup lang="ts">
const isOpen = ref(false);

defineShortcuts({
  meta_l: {
    usingInput: true,
    handler: () => {
      isOpen.value = !isOpen.value;
    },
  },
  // Fix: при русской раскладке не воркает
  meta_д: {
    usingInput: true,
    handler: () => {
      isOpen.value = !isOpen.value;
    },
  },
});
</script>

<template>
  <div>
    <UButton
      icon="i-heroicons-adjustments-vertical-20-solid"
      size="xs"
      color="gray"
      variant="ghost"
      @click="isOpen = true"
    ></UButton>

    <UModal v-model="isOpen">
      <UCard
        :ui="{
          ring: '',
          divide: 'divide-y divide-gray-100 dark:divide-gray-800',
        }"
      >
        <template #header>
          <h2 class="text-lg font-bold">Управление окружениями</h2>
        </template>

        <div class="flex flex-col gap-[12px]">...</div>

        <template #footer>
          <div class="flex flex-row items-center gap-[8px]">
            <UButton label="Сохранить"></UButton>
            <UButton
              label="Закрыть"
              color="gray"
              variant="solid"
              @click="isOpen = false"
            ></UButton>
          </div>
        </template>
      </UCard>
    </UModal>
  </div>
</template>
