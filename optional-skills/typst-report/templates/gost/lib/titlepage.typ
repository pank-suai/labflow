#let titlepage(
  title: "",
  subject: "",
  kind: "",
  author: "",
  group: "",
  university: "",
  faculty: "",
  department: "",
  teacher: "",
  city: "",
  date: "",
) = {
  set page(paper: "a4", margin: (top: 20mm, bottom: 20mm, left: 20mm, right: 15mm))
  set text(font: "Times New Roman", size: 12pt, lang: "ru", hyphenate: false)

  align(center)[
    #if university != "" [#university\ ]
    #if faculty != "" [#faculty\ ]
    #if department != "" [#department\ ]
    #v(3cm)
    #if kind != "" [#text(weight: "bold")[#kind]]
    #v(1cm)
    #text(size: 16pt, weight: "bold")[#title]
    #if subject != "" [#v(0.5cm) #subject]
    #v(3cm)
    #if teacher != "" [Преподаватель: #teacher\ ]
    #if author != "" [Выполнил: #author\ ]
    #if group != "" [Группа: #group\ ]
    #v(2cm)
    #if city != "" [#city\ ]
    #if date != "" [#date]
  ]
  pagebreak()
}
