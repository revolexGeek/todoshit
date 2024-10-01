<template>
  <div class="flex items-center flex-row gap-[12px]">
    <div class="flex flex-row items-center gap-[4px]">
      <UKbd v-if="showMeta">{{ metaSymbol }}</UKbd>
      <UKbd>{{ bind }}</UKbd>
    </div>
    <span class="text-md">{{ description }}</span>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  bind: String;
  description: String;
  showMeta: Boolean;
}>();

const { metaSymbol } = useShortcuts();
</script>
