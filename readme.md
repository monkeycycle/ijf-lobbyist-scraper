# Manitoba lobbyist registry scraper 

Michael Pereira <michael@monkeycycle.org>

Simple scraper to pull details from Manitoba's lobbyist registry.



* The registry includes an ID for the registration but not the individual. 




## Get started

pipenv for virtual machine and dependencies.

* `pipenv install`
* `pipenv shell`
* `python get_mb.py`




## Manitoba fields to grab


Registration ID; Submitted by lobbyist on; Accepted by Registrat on; Senior Officer Contact Information (Surname, First Name, Middle Name, Address, E-mail Address, Phone Number, Fax Number); Organization Information (Name of organization, Organization business or activity summary, Address, E-mail Address, Phone Number, Fax Number); Organization Lobbying Activity (Registration start date, Registration end date); Organization's Relevant Interfaces; Description of Organization (Description of Organization, Name of Officer); Corporation Information (Name of Director); Subsidiary Business Contact Information (Business Name, Mailing Address, Phone Numbers and E-mail); Controlling Corporation Business Contact Information (Business Name, Mailing Address, Phone Numbers and E-mail); Government or Government Agency Funding (Name of Government or Government Agency Funding, Amount of Funding); Organization Lobbyists (Lobbyist Name, Date Added, Date Inactivated, Active (This is a tick box), Lobbying Activities). Underneath Lobbying Activities there's a View button which is clickable. Lobbyist Information (Name, Start Date); Lobbying Activity Subject Matter (Subject Matter, Intended Outcome, Details of subject matter and intended outcomes); Target Contacts (Target, Name of Person Targeted, Title, Agency, Office or Constituency, Associated Minister/MLA, Date Added)
