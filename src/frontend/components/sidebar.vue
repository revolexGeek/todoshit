<script setup lang="ts">
const isOpen = ref(false);
const { metaSymbol } = useShortcuts();

defineShortcuts({
  meta_h: {
    usingInput: true,
    handler: () => {
      isOpen.value = !isOpen.value;
    },
  },
  // Fix: при русской раскладке не воркает
  meta_р: {
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
      color="gray"
      variant="ghost"
      icon="i-heroicons-information-circle-20-solid"
      square
      padded
      @click="isOpen = true"
    />

    <USlideover
      v-model="isOpen"
      side="left"
      class="overflow-y-auto overflow-x-hidden"
    >
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

          <div class="flex flex-col gap-[8px]">
            <h1 class="text-lg font-bold">Информация</h1>
            <p class="text-md">
              Здесь отображены основные аспекты, которые нужны при использовании
              приложения
            </p>
          </div>
        </template>

        <div class="h-full w-full flex flex-col gap-[16px]">
          <div class="flex flex-col gap-[12px]">
            <h3 class="text-sm font-bold">Горячие клавиши</h3>
            <Shortcut
              bind="P"
              description="Панель быстрых действий"
              showMeta="true"
            ></Shortcut>
            <Shortcut
              bind="H"
              description="Панель информации"
              showMeta="true"
            ></Shortcut>
            <Shortcut
              bind="O"
              description="Смена темы"
              showMeta="true"
            ></Shortcut>
            <Shortcut
              bind="L"
              description="Управление окружениями"
              showMeta="true"
            ></Shortcut>
            <Shortcut bind="ESC" description="Закрыть панель"></Shortcut>
          </div>
          <div class="flex flex-col gap-[12px]">
            <h3 class="text-sm font-bold">Теги</h3>
            <div class="flex flex-row items-center gap-[8px]">
              <UButton
                icon="i-heroicons-plus"
                size="2xs"
                color="gray"
                variant="solid"
              ></UButton>
              Добавить новый тег
            </div>
            <div class="flex flex-row items-center gap-[8px]">
              <UBadge label="Срочное" color="red"></UBadge>
              Изменить тег (нажатие)
            </div>
          </div>
          <div class="flex flex-col gap-[12px]">
            <h3 class="text-sm font-bold">Записка</h3>
            <div class="flex flex-row items-center gap-[8px]">
              <UButton
                label="Подробнее"
                icon="i-heroicons-chevron-right"
              ></UButton>
              Режим редактирования
            </div>
            <div class="flex flex-row items-center gap-[8px]">
              <UIcon name="i-heroicons-clock" size="20"></UIcon>
              Время создания
            </div>
          </div>
          <div class="flex flex-col gap-[12px]">
            <h3 class="text-sm font-bold">Другое</h3>
            <div class="flex flex-row items-center gap-[8px]">
              <UButton
                icon="i-heroicons-sun-20-solid"
                color="black"
                variant="solid"
              />
              Тема приложения
            </div>
            <div class="flex flex-row items-center gap-[8px]">
              <UChip>
                <UButton
                  label="Действия"
                  color="black"
                  variant="solid"
                  icon="i-heroicons-forward"
                />
              </UChip>
              Панель быстрых действий
            </div>
          </div>
        </div>

        <template #footer>
          <div class="flex flex-row items-center justify-end w-full">
            <UButton
              @click="isOpen = false"
              color="white"
              variant="solid"
              label="Закрыть"
            ></UButton>
          </div>
        </template>
      </UCard>
    </USlideover>
  </div>
</template>
