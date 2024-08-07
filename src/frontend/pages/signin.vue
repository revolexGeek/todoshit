<script setup lang="ts">
import { z } from "zod";
import type { FormSubmitEvent } from "#ui/types";

const toast = useToast();
const { signIn, token } = useAuth();

const schema = z.object({
  username: z.string().min(4, "Минимум 4 символа"),
  password: z.string().min(8, "Минимум 8 символов"),
});

type Schema = z.output<typeof schema>;

const state = reactive({
  username: undefined,
  password: undefined,
});

const isLoading = ref(false);

async function onSubmit(event: FormSubmitEvent<Schema>) {
  event.preventDefault();
  try {
    isLoading.value = true;
    await signIn(
      {
        username: event.data.username,
        password: event.data.password,
      },
      { callbackUrl: "/" }
    );
    toast.add({
      title: "Вход выполнен успешно!",
      description: "Вы вошли в личный кабинет.",
    });
  } catch (error) {
    toast.add({
      title: "Не удалось войти в аккаунт!",
      description: "Проверьте вводимые данные и повторите попытку.",
      color: "red",
    });
    console.log(error);
  } finally {
    isLoading.value = false;
  }
}
</script>

<template>
  <div class="flex flex-col gap-[16px]">
    <div class="flex flex-col gap-[8px] mb-3">
      <h1 class="text-xl font-bold">Войдите в аккаунт</h1>
      <p class="text-md">
        Чтобы получить доступ к функционалу приложения, пожалуйста, войдите в
        ваш аккаунт
      </p>
      <p class="text-sm">
        Еще нет аккаунта?
        <NuxtLink href="#" class="underline">Регистрация</NuxtLink>
      </p>
    </div>
    <UDivider></UDivider>
    <UForm
      :schema="schema"
      :state="state"
      class="space-y-4"
      @submit.prevent="onSubmit"
    >
      <UFormGroup label="Имя пользователя" name="username">
        <UInput v-model="state.username" />
      </UFormGroup>
      <UFormGroup label="Пароль" name="password">
        <UInput v-model="state.password" type="password" />
      </UFormGroup>
      <div class="flex flex-row flex-wrap items-center gap-[8px]">
        <UButton type="submit" :loading="isLoading"> Войти </UButton>
      </div>
    </UForm>
  </div>
</template>
