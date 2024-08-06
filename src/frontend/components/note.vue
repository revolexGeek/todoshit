<template>
  <UCard>
    <template #header>
      <h3 class="text-lg font-bold">{{ title }}</h3>
    </template>
    <div class="w-full h-fit flex flex-col gap-[12px]">
      <p class="text-md">{{ description }}</p>
      <div class="flex flex-row flex-wrap items-center gap-[8px]">
        <UBadge label="Срочное" color="red"></UBadge>
        <UBadge label="До завтра" color="yellow"></UBadge>
        <UButton
          icon="i-heroicons-plus"
          size="2xs"
          color="gray"
          variant="solid"
        ></UButton>
      </div>
    </div>
    <template #footer>
      <div class="flex flex-row items-center gap-[16px] justify-between">
        <div class="flex flex-row items-center gap-[8px]">
          <UIcon name="i-heroicons-clock" size="20"></UIcon>
          <span class="text-md">12 минут назад</span>
        </div>
        <div class="flex flex-row items-center gap-[8px] flex-wrap">
          <UButton label="Подробнее" icon="i-heroicons-chevron-right"></UButton>
        </div>
      </div>
    </template>
  </UCard>
</template>

<script setup lang="ts">
defineProps<{
  title: String;
  description: String;
}>();
</script>
