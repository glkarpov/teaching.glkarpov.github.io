# Кастомизация сайта

Этот документ описывает, как кастомизировать сайт на Quarto.

## Структура кастомизации

### 1. Стили (SCSS/CSS)

- `custom.scss` - основные кастомные стили в формате SCSS
- `custom.css` - дополнительные стили в формате CSS

Эти файлы автоматически подключаются через `_quarto.yml`:

```yaml
format:
  html:
    theme:
      - cosmo
      - custom.scss
    css: custom.css
```

### 2. Расширения (Extensions)

Папка `_extensions/custom/` содержит кастомные расширения Quarto.

Для активации расширения раскомментируйте в `_quarto.yml`:

```yaml
filters:
  - custom
```

### 3. Темы

Текущая тема: `cosmo`. Можно изменить в `_quarto.yml`:

```yaml
format:
  html:
    theme:
      - cosmo  # или cerulean, journal, flatly, darkly, и т.д.
      - custom.scss
```

Доступные темы: https://quarto.org/docs/output-formats/html-themes.html

### 4. Навигация

Навигация настраивается в секции `website.navbar` файла `_quarto.yml`.

### 5. Добавление новых страниц

Просто создайте новый `.md` файл в корне или в подпапке. Quarto автоматически добавит его в навигацию (если не указано `toc: false`).

## Примеры кастомизации

### Изменение цветов

В `custom.scss`:

```scss
:root {
  --teaching-primary: #2563eb;
  --teaching-secondary: #64748b;
}
```

### Кастомные компоненты

Можно создать Lua фильтры в `_extensions/custom/` для кастомных компонентов (как в курсах linalg_mds_25 и cu25).

