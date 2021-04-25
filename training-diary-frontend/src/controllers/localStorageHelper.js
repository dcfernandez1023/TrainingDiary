export const setStorageItem = (key, value) => {
  window.localStorage.setItem(key.toString(), value.toString());
}

export const getStorageItem = (key) => {
  return window.localStorage.getItem(key.toString());
}
