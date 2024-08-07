<template>
  <div class="flex flex-col gap-[16px]">
    <div class="flex flex-col gap-[8px]">
      <h1 class="text-xl font-bold">Выйти из аккаунта</h1>
      <p class="text-md">
        Вы сможете зайти в свой аккаунт если пройдете авторизацию по новой.
      </p>
    </div>
    <div class="flex flex-row items-center gap-[8px] w-full">
      <UButton
        :loading="isLoading"
        label="Выйти"
        color="red"
        @click="() => signOut({ callbackUrl: '/' })"
        icon="i-heroicons-link-slash"
      ></UButton>
      <UButton
        :loading="isLoading"
        label="Я передумал"
        to="/"
        variant="ghost"
        color="gray"
      ></UButton>
    </div>
  </div>
</template>

<script setup lang="ts">
const { signOut } = useAuth();
const isLoading = ref(false);
const toast = useToast();

async function logout() {
  try {
    isLoading.value = true;
    await signOut({ callbackUrl: "/" });
    toast.add({
      title: "Вы вышли из аккаунта!",
      description: "Выход из аккаунта был произведен успешно.",
    });
  } catch (error) {
    toast.add({
      title: "Ошибка выхода из аккаунта!",
      description: "Не получилось выйти из аккаунта, повторите попытку позже.",
    });
  } finally {
    isLoading.value = false;
  }
}
</script>
