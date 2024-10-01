<script setup lang="ts">
import { z } from "zod";
import type { FormSubmitEvent } from "#ui/types";

const toast = useToast();
const { signIn } = useAuth();

const schema = z
  .object({
    username: z.string().min(4, "Минимум 4 символа"),
    email: z.string().email("Некорректный Email").min(1, "Минимум 1 символ"),
    password1: z.string().min(8, "Минимум 8 символов"),
    password2: z.string().min(8, "Минимум 8 символов"),
  })
  .refine((data) => data.password1 === data.password2, {
    message: "Passwords don't match",
    path: ["password2"],
  });

type Schema = z.output<typeof schema>;

const state = reactive({
  username: undefined,
  email: undefined,
  password1: undefined,
  password2: undefined,
});

const isLoading = ref(false);

async function onSubmit(event: FormSubmitEvent<Schema>) {
  event.preventDefault();
  try {
    isLoading.value = true;
    const response = await $fetch("http://127.0.0.1:8000/api/auth/register/", {
      method: "POST",
      body: {
        username: event.data.username,
        email: event.data.email,
        password1: event.data.password1,
        password2: event.data.password2,
      },
    });

    await signIn(
      {
        username: event.data.username,
        password: event.data.password2,
      },
      { callbackUrl: "/" }
    );
    toast.add({
      title: "Регистрация выполнена успешно!",
      description: "Вы были зарегистрированы.",
    });
  } catch (error) {
    toast.add({
      title: "Не удалось зарегистрироваться!",
      description:
        "Возможно, пользователь уже зарегистрирован или слишком слабый пароль.",
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
      <h1 class="text-xl font-bold">Зарегистрируйтесь</h1>
      <p class="text-md">
        Чтобы получить доступ к функционалу приложения, пожалуйста, войдите в
        зарегистрируйтесь
      </p>
      <p class="text-sm">
        Уже есть аккаунт?
        <NuxtLink href="/signin" class="underline">Вход</NuxtLink>
      </p>
    </div>
    <UDivider></UDivider>
    <UForm :schema="schema" :state="state" class="space-y-4" @submit="onSubmit">
      <UFormGroup label="Имя пользователя" name="username">
        <UInput v-model="state.username" />
      </UFormGroup>
      <UFormGroup label="Email" name="email">
        <UInput v-model="state.email" />
      </UFormGroup>
      <UFormGroup label="Пароль" name="password">
        <UInput v-model="state.password1" type="password" />
      </UFormGroup>
      <UFormGroup label="Пароль (Повтор)" name="password2">
        <UInput v-model="state.password2" type="password" />
      </UFormGroup>
      <div class="flex flex-row flex-wrap items-center gap-[8px]">
        <UButton type="submit" :loading="isLoading">
          Зарегистрироваться
        </UButton>
      </div>
    </UForm>
  </div>
</template>
