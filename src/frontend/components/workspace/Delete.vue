<template>
  <UButton
    @click="open = true"
    icon="i-heroicons-x-mark-20-solid"
    color="red"
    variant="solid"
  ></UButton>
  <UModal v-model="open">
    <UCard
      :ui="{
        ring: '',
        divide: 'divide-y divide-gray-100 dark:divide-gray-800',
      }"
    >
      <template #header>
        <h3 class="text-xl font-bold">Удаление окружения</h3>
      </template>

      <div class="flex flex-col gap-[16px]">
        <p class="text-md">
          Вы уверены что хотите удалить окружение <b>{{ workspace_.name }}</b
          >?
        </p>
        <p class="text-xs text-red-400">
          Данное действие нельзя отменить, будьте осторожны!
        </p>
      </div>

      <template #footer>
        <div class="flex flex-row items-center gap-[8px] flex-wrap">
          <UButton
            class="rounded-md"
            label="Удалить"
            icon="i-heroicons-trash-20-solid"
            color="red"
            variant="solid"
            @click="deleteWorkspace(workspace_.id)"
            :loading="isLoading"
          ></UButton>
          <UButton
            label="Я передумал"
            color="gray"
            variant="ghost"
            @click="open = false"
            :loading="isLoading"
          ></UButton>
        </div>
      </template>
    </UCard>
  </UModal>
</template>

<script setup lang="ts">
import type IWorkspace from "~/types/workspace";
const open = ref(false);

const workspace = useWorkspaceStore();
const isLoading = ref(false);

async function deleteWorkspace(id: number | string) {
  isLoading.value = true;
  await workspace.deleteWorkspace(id);
  await workspace.fetchWorkspaces();
  isLoading.value = false;
  open.value = false;
}

defineProps<{
  workspace_: IWorkspace;
}>();
</script>
