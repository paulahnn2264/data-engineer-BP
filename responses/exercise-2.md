# Exercise 2

## Business Process Description

I'll be modeling BP's climbing gym business. In this I'll be making sure to hit key points that are important for climbing gyms and specifically our own. I'd be happy to talk about this more - in the interest of time i spent about the recommended amount of time on this, not being very familiar with specifically fact tables, though given more time and context, I'm sure i'd be able to give a better answer

## Fact Table

| Column Name | Type | Description |
| --- | --- | --- |
| Column Name | Type | Description |
| member phone number | int | ID for each member given at time of registration |
| member birthdate | datetime | member birthday |
| member type | varchar | type of membership |
| member waiver | bool | active waiver on file |
| member active | bool | active membership or not |
| member start | datetime | when the membership started |
| member last check in | datetime | when the member last checked in |

## Dimension
| --- | --- | --- |
| member | int | main dimension table with all inforamtion about the member |
| location | varchar | gym location |



