export const exercise = {
  exercise_id: "",
  user_id: "",
  name: "",
  category: "",
  sets: 0,
  reps: 0,
  amount: 0,
  units: ""
};

export const exerciseFields = [
  "exercise_id",
  "user_id",
  "name",
  "category",
  "sets",
  "reps",
  "amount",
  "units"
];

export const exerciseMetaData = {
  exercise_id: {
    type: "string",
    editable: false,
    displayName: "",
    elementType: "",
    options: [],
  },
  user_id: {
    type: "string",
    editable: false,
    displayName: "",
    elementType: "",
    options: [],
  },
  name: {
    type: "string",
    editable: true,
    displayName: "Name",
    elementType: "input",
    options: []
  },
  category: {
    type: "string",
    editable: true,
    displayName: "Category",
    elementType: "select",
    options: ["Weight-lifting", "Body-weight", "Stretching", "Cardio", "Recovery", "Other"]
  },
  sets: {
    type: "number",
    editable: true,
    displayName: "Sets",
    elementType: "input",
    options: []
  },
  reps: {
    type: "number",
    editable: true,
    displayName: "Reps",
    elementType: "input",
    options: []
  },
  amount: {
    type: "number",
    editable: true,
    displayName: "Amount",
    elementType: "input",
    options: []
  },
  units: {
    type: "string",
    editable: true,
    displayName: "Units",
    elementType: "select",
    options: ["lbs.", "kgs."]
  }
};
