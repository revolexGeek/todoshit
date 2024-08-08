<script setup lang="ts">
import { z } from "zod";
import type { FormSubmitEvent } from "#ui/types";
import type IWorkspace from "~/types/workspace";

const workspace = useWorkspaceStore();
const isOpen = ref(false);
const isLoading = ref(false);

const schema = z.object({
  name: z.string().min(3, "Минимум 3 символа").max(64, "Максимум 64 символа"),
});

type Schema = z.output<typeof schema>;

const state = reactive({
  name: undefined,
});

async function onSubmit(event: FormSubmitEvent<Schema>) {
  event.preventDefault();
  isLoading.value = true;
  await workspace.patchWorkspace(props.workspace_.id, event.data.name);
  await workspace.fetchWorkspaces();
  isLoading.value = false;
  isOpen.value = false;
}

const props = defineProps<{
  workspace_: IWorkspace;
}>();
</script>

<template>
  <div>
    <UButton
      color="blue"
      icon="i-heroicons-ellipsis-vertical-20-solid"
      @click="isOpen = true"
    />

    <USlideover v-model="isOpen">
      <UCard
        class="flex flex-col flex-1"
        :ui="{
          body: { base: 'flex-1' },
          ring: '',
          divide: 'divide-y divide-gray-100 dark:divide-gray-800',
        }"
      >
        <template #header>
          <UButton
            color="gray"
            variant="ghost"
            size="sm"
            icon="i-heroicons-x-mark-20-solid"
            class="flex sm:hidden absolute end-5 top-5 z-10"
            square
            padded
            @click="isOpen = false"
          />

          <h2 class="text-lg font-bold">Изменение окружения</h2>
        </template>

        <div class="flex flex-col gap-[16px]">
          <p class="text-md">
            Чтобы продолжить, укажите новое название для окружения:
          </p>
          <UForm
            :schema="schema"
            :state="state"
            class="space-y-4"
            @submit="onSubmit"
          >
            <UFormGroup label="Название" name="name">
              <UInput
                v-model="state.name"
                type="text"
                :placeholder="workspace_.name"
              ></UInput>
            </UFormGroup>
            <UButton
              type="submit"
              :loading="isLoading"
              label="Изменить"
              icon="i-heroicons-ellipsis-vertical"
            >
            </UButton>
          </UForm>
        </div>

        <template #footer>
          <div
            class="flex flex-row items-center gap-[8px] flex-wrap justify-end"
          >
            <UButton
              :loading="isLoading"
              color="gray"
              variant="ghost"
              label="Отмена"
              @click="isOpen = false"
            ></UButton>
          </div>
        </template>
      </UCard>
    </USlideover>
  </div>
</template>
