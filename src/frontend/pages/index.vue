<template>
  <div
    v-if="status === 'authenticated' && user"
    class="flex flex-col gap-[16px]"
  >
    <h1 class="text-xl font-bold">С возвращением, {{ user.username }}</h1>
    <NoteList></NoteList>
  </div>
  <div v-else-if="status === 'loading'" class="flex flex-col gap-[16px]">
    <UProgress></UProgress>
    <USkeleton class="w-full h-[120px]"></USkeleton>
    <USkeleton class="w-full h-[200px]"></USkeleton>
    <USkeleton class="w-full h-[60px]"></USkeleton>
    <USkeleton class="w-full h-[20px]"></USkeleton>
  </div>
  <div v-else class="flex flex-col gap-[16px]">
    <div class="flex flex-col gap-[8px]">
      <h1 class="text-xl font-bold">Войдите в аккаунт</h1>
      <p class="text-md">
        Чтобы начать использовать приложение, пожалуйста, войдите в аккаунт или
        зарегистрируйтесь
      </p>
    </div>
    <div class="flex flex-row flex-wrap items-center gap-[8px]">
      <UButton to="/signup" label="Регистрация"></UButton>
      <UButton
        to="/signin"
        label="Вход"
        variant="solid"
        color="black"
      ></UButton>
    </div>
  </div>
</template>

<script setup lang="ts">
const { status, data: user } = useAuth();
</script>
