<script setup lang="ts">
const isOpen = ref(false);

defineShortcuts({
  meta_p: {
    usingInput: true,
    handler: () => {
      isOpen.value = !isOpen.value;
    },
  },
  // Fix: при русской раскладке не воркает
  meta_з: {
    usingInput: true,
    handler: () => {
      isOpen.value = !isOpen.value;
    },
  },
});

const people = [
  { id: 1, label: "Создать новую заметку", icon: "i-heroicons-plus" },
  { id: 2, label: "Просмотреть заметки", icon: "i-heroicons-eye" },
  { id: 3, label: "Сменить окружение", icon: "i-heroicons-arrow-path" },
  {
    id: 4,
    label: "Настроить окружение",
    icon: "i-heroicons-adjustments-vertical",
  },
  { id: 5, label: "Открыть справку", icon: "i-heroicons-information-circle" },
  { id: 6, label: "Сменить тему", icon: "i-heroicons-sun" },
  {
    id: 7,
    label: "Открыть репозиторий на Github",
    icon: "i-heroicons-sparkles",
  },
];

const selected = ref([]);
</script>

<template>
  <div>
    <UChip>
      <UButton
        label="Действия"
        color="black"
        variant="solid"
        icon="i-heroicons-forward"
        @click="isOpen = true"
      />
    </UChip>

    <UModal v-model="isOpen">
      <UCommandPalette
        v-model="selected"
        multiple
        nullable
        :groups="[{ key: 'people', commands: people }]"
      />
    </UModal>
  </div>
</template>
