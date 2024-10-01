<script setup lang="ts">
const isOpen = ref(false);
const isLoading = ref(true);
const workspace = useWorkspaceStore();

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

async function load() {
  isLoading.value = true;
  await workspace.fetchWorkspaces();
  isLoading.value = false;
}

load();
</script>

<template>
  <div>
    <UButtonGroup @click="isOpen = true" class="hover:cursor-pointer">
      <UBadge
        size="xs"
        :color="[workspace.selectedWorkspace ? 'primary' : 'red']"
        ><UIcon
          name="i-heroicons-adjustments-vertical"
          size="20"
          variant="solid"
        ></UIcon
      ></UBadge>
      <UButton variant="solid" color="gray">
        <p class="truncate max-w-[128px] text-xs">
          {{
            workspace.selectedWorkspace
              ? workspace.selectedWorkspace.name
              : "Окружение не выбрано"
          }}
        </p>
      </UButton>
    </UButtonGroup>

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

        <div class="flex flex-col gap-[16px]">
          <div class="flex flex-col gap-[8px]">
            <h3 class="text-md font-bold">Ваши окружения:</h3>
            <div
              v-if="isLoading"
              class="flex flex-row flex-wrap items-center gap-[8px]"
            >
              <USkeleton class="w-[120px] h-[36px]"></USkeleton>
              <USkeleton class="w-[60px] h-[36px]"></USkeleton>
              <USkeleton class="w-[30px] h-[36px]"></USkeleton>
              <USkeleton class="w-[16px] h-[36px]"></USkeleton>
              <USkeleton class="w-[8px] h-[36px]"></USkeleton>
            </div>
            <ul class="flex flex-row flex-wrap items-center gap-[8px]" v-else>
              <li
                v-for="workspace__ in workspace.workspaces"
                :key="workspace__.id"
              >
                <WorkspaceSelect :workspace_="workspace__"></WorkspaceSelect>
              </li>
              <WorkspaceCreate></WorkspaceCreate>
            </ul>
          </div>

          <UCard>
            <div class="flex flex-col gap-[16px]">
              <div class="flex flex-row items-center gap-[8px]">
                <h4 class="text-md font-bold">Подсказка</h4>
                <UIcon
                  name="i-heroicons-information-circle-20-solid"
                  size="20"
                ></UIcon>
              </div>

              <p class="text-sm">
                Нажмите на бейджик нужного окружения для установки, или же,
                нажмите на крестик рядом с нужным окружением чтобы удалить его.
              </p>
            </div>
          </UCard>
        </div>

        <template #footer>
          <div class="flex flex-row items-center justify-end gap-[8px]">
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
