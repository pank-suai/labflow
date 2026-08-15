#let title_page(
  title: "",
  subject: "",
  kind: "",
  author: "",
  group: "",
  university: "",
  faculty: "",
  department: "",
  city: "",
) = {
  align(center)[
    #if university != "" [#university\ ]
    #if faculty != "" [#faculty\ ]
    #if department != "" [#department\ ]
    #v(3cm)
    #text(weight: "bold")[#kind]
    #v(1cm)
    #text(size: 16pt, weight: "bold")[#title]
    #if subject != "" [#v(0.5cm) #subject]
    #v(4cm)
    #if author != "" [Выполнил: #author\ ]
    #if group != "" [Группа: #group\ ]
    #v(2cm)
    #if city != "" [#city, ]
    #datetime.today().year()
  ]
}
