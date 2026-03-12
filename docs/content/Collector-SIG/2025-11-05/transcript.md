SIG: Collector SIG
Date: 2025-11-05
Duration: 52 minutes
Zoom Recording URL: https://zoom.us/rec/share/rTquogjqqjyC_v_QAJ55zhinIXOwi1cdeRoXt1iy6SXTA5quQrWB0psHulhyDQ1Y.nYmh9bYbmfbbpiw6
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 06:53 Hey.
**Dmitrii Anoshin** 07:00 Hi, everyone.
**Ernest Owojori** 07:08 Hi, everyone. Good day.
**kushal** 07:27 Guys, do we have separate meeting for collector and… collector country?
**Pablo Baeyens** 07:34 No, it's only one meeting.
There are different… it happens at different times, depending on the week, so that people across the world can join, but it's one meeting for… all the collector Sq repositories.
**kushal** 07:48 Got it.
**Pablo Baeyens** 08:05 I think we can get started, Ernest, if you want to go ahead?
**Ernest Owojori** 08:12 Okay, thank you, sorry, I didn't know what was spoken last time, but thank you.
Apologies, I might not be able to on my video.
It's dark here, and, you know… The condition in my countries.
There are no stable electricity. So, but I'm going to share my screen.
And I would like to ask how many minutes I've got to… present the initial analysis that I have.
Because, I would like to know what to show. I want not to show based on the time.
I don't know if you got that.
**Pablo Baeyens** 09:01 Well, you can see your Chrome screen, right now on the Zoom tab.
**Ernest Owojori** 09:07 Yes, I was trying to confirm how many minutes do I have for this short presentation.
**Pablo Baeyens** 09:12 Oh, I'm in… You can go ahead and, we'll stop you if it gets too long, but, you can… top product.
**Ernest Owojori** 09:20 Thank you.
Okay, thank you.
Hmm… Yeah, so… I am the LFX mentee that is developing the data analysis guide, which I believe every SIG will find useful when we are done.
But, because, the hotel collector follow-up survey happened to conclude when I joined, so I chose to analyze the survey and use it as my… one of the reference surveys for my guide.
So I've come here to present, the initial analysis that I have.
With the so-heim of getting more questions from the collector, because… the collector seek, so… because I believe, those that work with collectors, we ask the best questions when it comes to, the kind of answer… question we should be answering.
So, in my… general guide, I used to… encouraged to have a plan before we start analysis, which is where I mostly need our input. So, currently, I have tried to prepare the general EDA, where I said.
all variables to be analyzed or visualized to know responses per respondent in a particular way, and most importantly, cases where we need to do cross-tabulations, I tried With the help of… ChatGPT to create some questions, the ones that make sense to me, I accept them and I try to analyze them, and I would like us to help me ask more questions that make sense as users of these, tools day in, day out. Now, to the little result that I have shown so far.
I understand that, the interest of doing the follow-up survey is to note what has changed between last year and this year, but before I go to that, I try to show, you know, I'm going to give access to this document. I try to show, the general EDA and I'm going to try to show some important aspects that I think are important. I could see here that, greater percentage are 1,000 plus employees, and I'm going to propose to the end user seek to probably change the way we classify this based on the European, you know, Commission standard of Classifying the size of employees. Maybe they will accept or not.
Then, the rest of the insights you can come here to is just general EDA, and one thing that I importantly wanted to point out is, is in the comparison, but before I go there.
I just want to skim through this section.
Which I believe, You know, tries to answer… tries to put visualization into every single question we asked in the survey.
So, 2D comparison now.
Here, I tried to compare analysis that was done last year, And, try to give… The results for this year and see what has changed.
can we find answers to what has changed? So I could see here that the, you know, because last year, the way the more than 10 question year was asked is different.
I have to recategorize down to meet up to that scale, so I see that there's a 10% increase, but the question is, is the increase significant, which I may say, maybe not.
But more interestingly, insight from this year, in addition to last year, shows us here that people don't really use Ashikovs Nomad, and we can… the percentage of usage is negligible, and kubernetes still remains the most used, with the same percentage level, and there is some 18% increase in virtual machine… virtual machine usage.
maybe this is telling us something that we would absorb over the years, but maybe… and I believe you guys can say more to this.
Also, when it comes to Kubernetes deployment scenario, there has been little to no change, in my own opinion, in terms of differences over the years, but we could see that Gateway, obviously, is getting the highest frequency, but there has not been really changes over the years in terms of Kubernetes deployment scenarios. Then, okay.
I showed… I tried to show this with caution, because the way the question for… improvement was asked last year is different from the way it was asked this year. So, technically, we are not supposed to compare them, but I showed this because I wanted to Show that, stability… which was portrayed last year to be the highest doesn't necessarily mean that it is the highest. It just means that we did not give people options to pick more than one reason. Now that we were given more than one reason, people think that configuration management and resolution is the highest. And that could also ask the question whether some things have changed in the way open telemet generally has improved. That has changed the direction of this question, and we cannot necessarily infer that.
Now, to… Exporters, promoters, and the likes. I, I try to keep constant what was the top 5 last year, and see how they've changed this year, even though I have a better way of presenting this, but I have not implemented that, but I don't especially think I should talk about that now.
So, Ubuntai OHTP exporter still seems to be dominating, and changes across this… I may not necessarily be seeing whether they are significant or not, but we could see how they dropped across the top 5. I could see that Prometheless Exporters seems to… got an increase in usage. I most likely have moved away from being Top 5 to probably top 2. But by the time I show the inside for 2025, that would be clear.
And I'm more curious about to know what the people that, I mean, the collector thinks about this kind of insights. Then, for receivers, Where TP receiver is still very much high.
And, the file receiver also got very, very much increased. I don't, I don't know… what could have caused that, but I believe, maybe the people in the community could give very good explanations to that.
So this goes on to processors and connectors.
And then extensions.
More importantly, I… some of the questions I asked, here that are cross-stabulations, I try to put them into Tables and resorts.
So, yeah, does organization size really predict running OpenTelemetry in production? From the result I see… I see here.
I would say that I cannot make the inference that organization size predicts running OpenTelemetry in production, because, Cases where the sample size is below 20, even… scientific… let me say, according to classroom knowledge, they say 30, that we cannot especially infer, but at least I'm sure I can infer on 1,000 plus employees, which is 75, so… and the difference… Yeah, I can't necessarily say. The changes in organization size predict open telemetry in production, even though there's a way to take these insights a step further, but I'm a little bit weary of losing the interpretation to people that are non-technical.
Don't, there are other questions here that I try to answer that those team-type project deployment environments, you know, I could… I could see here that cases where, you know, observability sort of have… Kubernetes seems to really, really drag attention depending… irrespective of the team types, but when you move away from Kubernetes and virtual machine, the rest is little to… no calling attention. Then, for what kind of quality deployment scenario, you know, does it align with the specific usage of number of collectors? I could see here that as the number of collectors increases, people tend to use Gateway and Demostat.
Then, those organization size predict the use of processors? I could see that batch processors is mostly used At least for organizations that are above 100.
This is difficult to infer, because, you know, even organizations that are not above 100, they are still the most used down… down the column.
But we could see that bad processors seems to really, really be used. And one interesting thing I see here is memory limiter being 63% In 50th to 99.
employees. I don't really know what to infer, because I don't know what memory limiters have been used for, and I'm happy to hear our opinion across all this. These insights will still be later presented to us in more detail, but I want to get our questions, you know, the way we want the questions to be asked in the document that I've prepared. I would like us to Help me collaborate so that we can come up with the best question And present this report in a more.
full, or let me say exhaustive insights. So, one thing I also noticed here in… when we asked the question of those maturity level really predict processors being used, I also see some contrastion around expert level, those that have already established observability practices, seems to be very familiar with patch processor, attribute, and filter, and, you know, there's a little… Clear pattern in terms of beginners being… You know, very scanty when it comes to batch processors down the line like this.
And when we try to also hack those organization-sized bridge connectors being used, you know, I really cannot make An interesting insight, apart from OHTP comprising of 50% of you know, 50 to 99 employees. So, these are the insights I've been able to carve together that most of them don't make sense to me, because I don't use, you know.
collector in my daily usage, but I believe that if we can collaborate with me to ask the best question, and I bring out what the data is saying here.
I mean, the best questions.
In this sheet.
I already added it to our meeting.
**Pablo Baeyens** 20:34 The document you shared on… on the meeting notes?
**Ernest Owojori** 20:38 Yes, yes. This one.
**Pablo Baeyens** 20:41 Yeah. So, from my side, I'll take a quick look, maybe later this week. Thank you for all the analysis you've done. I'm… I think my only piece of feedback right now is that maybe some of the… It's something that we face with other surveys. When you start to divide into smaller groups, the sample size ends up being very small, and so there's a lot of noise, and it's very difficult to tell whether something is because of the noise, or because there's actually a pattern.
You could see that on, say, the questions about connectors, for example, that you were showing last.
And there were some… some of the buckets that were, like, 8 people, if I… or 8 responses.
**Ernest Owojori** 21:24 Yes, yes, yes.
**Pablo Baeyens** 21:26 Yeah, probably, too few to be able to confidently say there's an iron there, but thank you, this is interesting.
**Ernest Owojori** 21:35 Yes, I agree. So, you know, in my guide, I want to say that when the sample size is.
**Pablo Baeyens** 21:40 less than…
**Ernest Owojori** 21:41 Tati… you know, make insights, you know, sparringly. When it is less than 20, do not make insights.
Adobeat.
you know, that is what I want to put in my guide, and you know, maybe that… we could agree or disagree with that.
**Pablo Baeyens** 22:00 Cool. Yeah, so, as I said, I'll take a look at the document, and other people interested can do so, and you can continue sharing anything that can be publicly shared, you can do so in the Autel Collector Dev Slack channel, and Like, we can give you… Feedback on… Yeah, Audis.
**Ernest Owojori** 22:23 Yes, I'm going to share the…
**Pablo Baeyens** 22:24 Or whether a conclusion seems like noise, or seems like actually something interesting.
**Ernest Owojori** 22:29 Yeah, yeah, I'm going to share the… Document itself again.
Then, as I get your questions from the collector, if I have, initial insight, I'm happy to share it in the Slack channel. Thank you.
**Pablo Baeyens** 22:45 Nope.
Does anybody else have any other common feedback about this for Ernest?
Okay, if not, we can… we can move to the next one. Thank you, thank you for the presentation.
So, the next one is mine… I filed the issue this morning.
this one.
So… We've been having some discussions, Of course, like, provers and maintainers of the different collector repositories.
As you may know, we've discussed this on previous, SIG meetings, we are… trying to address some feedback that we got from the CNCF to, to get to graduation.
And, graduation being, like, a stage of the project for OpenTelemetry, where we get, sort of, the seal of approval from the foundation.
And so one thing that, a lot of… One thing that takes a significant amount of time from approvers and maintainers is, Sponsoring new components, reviewing them, making sure that they make sense and are aligned with the, Collector's egg, and… we… discussed that, well, this seems like a problem, and we want to make some sort of change to this process to make sure that Well, people can still build their own components and, like, contribute them if it makes sense, but, it… Needs less input or less work from… The approvers on my turners.
And there were proposals from… all the way going from, like, we should not accept any new components until OpenTechnatural graduates.
To, like, more intermediate things, like… encouraging people in some ways to build the components outside of official open storage repositories, before, before accepting them.
So yeah, I wanted to bring it up just to see if there was any… high-level proposals that I should add to the issue, or comments about the existing proposals, just so that we can We can keep the conversation going.
I see Christos received answer. Please go ahead.
**Christos Markou** 25:21 Yeah, thanks, Pablo. Yeah, first of all, as an approver of Contrib, I'm really supportive on this idea, focusing on quality over quantity and sustainability of the project. A few topics that we need to probably consider here is that, yeah, so topic A, we should clarify how components living outside the Contrib won't be considered, let's say, less good compared to those living, within Contrib repository.
And, this brings us to, like, issues about, that we might face about vendor fairness. We should also ensure that vendor X should not have more components on.
vendor Y in Contrib, and also we should also have, yeah, a fair process for component donation. We might have a case where two vendors have the same component maintained outside of Contrib? What if they want to both donate it? We should have a straight process for this. I can also comment on the issue directly, but just sharing this for the sake of discussion. There are any comments.
**Pablo Baeyens** 26:31 I didn't quite get the first one, like, the… clarifying how components living outside of Contrib are… What?
**Christos Markou** 26:38 Yeah.
Yeah, there might be the case that users or customers of vendors, consider components that are not hosted in Contrib as less good, because they are not living in Contrib, so they're not official, or things like that. Probably we can try to clarify this, or just improve our docs, and yeah, essentially work on this and clarify what is the case. If that's true, we need to consider about this. If that's not true, we need to explicitly document this and make it clear for users.
If that makes sense.
**Pablo Baeyens** 27:14 Yeah, okay, that makes sense, you know. Like, helping people have some sort of way of evaluating the quality of components, regardless of whether they are inside of or outside country. Okay, makes sense.
**Christos Markou** 27:24 Yeah, because if contrib is, like, the ultimate goal for components, then, yeah, we might have, like, people pushing for having their components in, so we need to, yeah, make sure that we have clear guidelines about this.
**Paulo Janotti** 27:46 I would like to mention, on the third topic about the code owners for components, I think more than the number, we need to… And we should announce that beforehand, I think.
I think we should be more aggressive and kind of unmaintain it and removing, in… when we have… long delays to get answers, you know. In a sense, of course, two or more is better, but it's better a component that we have one maintainer that's responsive than one that we have four that we don't get any of them to interact. So.
I think we should be a bit more aggressive in the process to say, hey, this component, code owners are not responding.
We are going to start the process, and the process has these dates to… to, Declare the component deprecated, and then remove it, you know?
**Pablo Baeyens** 28:58 Right.
Yeah, I think that makes sense. My… So the two code owners thing, I think mostly came from me, the reason I'm suggesting it is because I think it is an easy predictor of Like, it's going to… be more likely, if there are two or more code owners, that this is going to be maintained down the road, versus if there is one code owner. If we have other criteria, for example, if you're a… maybe if you're a community member from the GitHub org, you are more likely to keep around, or if you have shown that you can maintain other components, or have a role in some other repository in OpenTelemetry, those are also maybe good predictors that you'll stick around, and you will maintain your component.
So, we can look into those.
**Paulo Janotti** 29:51 Yeah, just, just to be clear, I'm… I'm not saying anything against the two, but I think that the goal is responsive, To get really responsive co-owners.
So, that's one of the ways to help with that, but then I think we… we should measure on our goal, on the thing that we really want to… but yeah, no, true, at least true is fine as a requirement.
**Pablo Baeyens** 30:25 Okay.
Any other comments?
Okay, it doesn't seem like it, The next topic is a component proposal, so, it could be useful to hear from the people proposing the component, like, how do you feel about this? If you were to, for example, host your components outside of Contrib, what would be the… the things that you would the problems that you would face, I guess.
**Rob Bavey** 31:16 I think that's a good question. I think… I'm Rob from Elastic. Yeah. I think hosting outside would be something we'd interest. We need to understand what the logistics are about doing that, how we'd work on the development model for doing that. I know, ideally, we'd like to do everything upstream, make sure we get full community approval for something like this, which has kind of, like, a broad, We just have a pretty broad, use case for it. So, you know, we're looking for adding, sort of enrichment processor and adding lookups in static and dynamic cases to the collector, which I think is a fairly core feature, which I think, ideally, we'd like to do upstream first, rather than, Rather than donated, that makes sense. I think we'd certainly be willing to have more than one cod owner for this, I think that would absolutely make sense for what we're proposing here.
but yeah, I don't know what other folks think about this.
**Pablo Baeyens** 32:15 Okay, so if I understand correctly, it's more about you fear that the component will be less widely used, or considered less… To have less buy-in from the community if it's hosted outside of country.
**Rob Bavey** 32:29 I think there's a couple of different things we can think about here. There's a buy-in from the community, and there's also, I don't know if we'll end up having… because there's been a couple of proposals around this kind of feature, like this, whether we'd end up with competing proposals, and we'd end up with a bifurcated, ecosystem, you know, way of doing lookups, which may be difficult to reconcile later, if there's things that kind of, like, have a fairly broad appeal and have more… a lot of folks interested in it. We've certainly had a lot of people who are interested in doing this. We've had a lot of, kind of, thumbs up and hearts.
But I want to make sure that, you know, I think ideally we'd like to do this in the upstream, so we get full community approval, and we don't… we end up with a single way of doing this.
**Pablo Baeyens** 33:13 Okay, perfect. Yeah, I'll let you speak about that specific proposal. Thank you for… For the feedback, that's useful.
**Rob Bavey** 33:22 Sure. So, yep, so we talked about this a few weeks ago. We're looking for a sponsor for enrichment processes to add enrichment capabilities into the hotel processor, a standard way of doing lookups. We're sort of looking at potentially ways of adding, static lookups and dynamic lookups, so static lookups would be, you know, would be things like, IP lookups, GOIP, Or, you know, another thing might be looking, you know, we might be looking at a YAML file where we want to update, you know, we want to enrich data with local information, but we also want to maybe want to do dynamic updates where we have an API that we want to… we want to, we want to hit, so we can do dynamic change, you know, things that change over time, so we can do… and, you know, the idea is we can have enrichment capabilities into DOTL collector in a standardized way, and that will eventually include doing things like, you know, adding general caching, And things along those. So, we've brought this up a couple of times before. One thing that has changed since the last time we brought this up is that Joao has created a draft PR, which shows the, initial scaffolding you know, which could give, like, a general PR approach for how we would plan to approach this, and shows the scaffolding of how we do this, so it shows a, So it includes a lookup processor, it includes a… a simple no-op extension module that shows how that would work, but there's a couple things we'd like to do there, which kind of shows how this would work in practice. As I want to think, I wanted to re-up this was, we can talk about this in person at KubeCon if folks want to reach out to us. We're happy to talk about it while we're there.
**Dmitrii Anoshin** 35:05 The only recommendation from my side is to look into the entity's working group and how this is evolving. So, essentially, going forward, like, all the enrichment processors would be… defined as entity enrichment processor. So, for example, resource detection processor. It would add entity to all the telemetry, for example, based on enabled detector. So if, let's say, I enable AWS detector and EC2 detector, for example, it means that I'm looking at existing, I'm… this collector is running on the EC2 host, and it adds An entity with the, like, specific… Model, where it has identified an attribute and descriptive attribute to all the telemetry associated, coming through that collector.
And it'll be the same for all of the other processors that are doing this kind of things, like, for example, Kubernetes.
Kubernetes attributes processor would also do enrichment of Kubernetes entities. So, for example, if it sees some data coming from a Kubernetes pod from the outside, it would add entity port associated with all the telemetry.
pod entity, associated with that telemetry, etc. So, I would just encourage to look in, into, like, entities, data model, maybe, maybe OTAP.
And see how enrichment processor would be… Defined, would work with entities, essentially.
Because, like, right now, the concept is adding, like, random attributes to the resource. This is how currently all the processors works.
All the processor work, and then all going forward, it'll, like, gradually shift toward entities.
**João Duarte** 37:12 Yeah, so I was involved in this as well. Rob mentioned this already. So, I think part of the reason why this was not heavily coupled in concept for entities is because it could be heavily related to an entity, again, like you mentioned with Amazon, but sometimes it is still an entity, but not immediately related to the collection that you did. So it could be… you could have all the distributed collection of data, and then it goes through one one collector, and that collector does enrichment for all of those sources, and that could come from a database, for example.
That category's interest.
**Dmitrii Anoshin** 37:52 But what's the information that would be enriched? What's the data that you add to the telemetry?
**João Duarte** 37:58 It is… and that is a good point. It could still be related to… to an entity, it's not just an entity, the database itself is just a source, and that source is not related to the entity itself, as Amazon is more related to the entity where we did the collection. Okay, the database is the source of the information, but the information itself that is being added, what is it?
Yeah, so it… I think we can call it an entity as well. It could be a department information, it could be a product category, it can be anything related to the data that you're working with. So, we can call it entities. I think that's the good and a bad thing of calling things entities, because we can call anything an entity.
**Dmitrii Anoshin** 38:39 But we have to… if we add in resource attributes, we have to make an entity to go forward, because we are… resource attributes is, like, going to be deprecated concept.
And everything should be as part of entity. It still would be reflected in the resource attribute for backward compatibility, but the components should clearly say what like, entities they are enriching data with. So if it's database as a source, right, but what we are taking from database, I don't know, like, entity being… a business unit, or something like that. And that, it can be dynamically configured in your processor, but that dynamic configuration should take, should provide interface to define entity instead of just random key-value pairs, that's what I'm saying.
**João Duarte** 39:31 Got it, Ed. Makes sense.
**Rob Bavey** 39:44 Thank you for that, yeah. As I said, we're, you know, there'll be folks at the KubeCon next week who can talk about this if you have any further questions, want to talk about that, or we can talk in the issue… ask these questions in the issues, too.
**Dmitrii Anoshin** 39:56 Sounds good. It's not like blocking requests from my site. You can still set everything as a resource attribute, but going forward, like, someone would have to work on that processor, if it's accepted and added to the contrib.
And, would change the configuration interface to, adopt, new entities interface.
So, it's just, like, at least thinking about that from the beginning would be beneficial.
**João Duarte** 40:27 And I think that's one of the reasons why, like, the discussion at the start of changing the discussion more at the donation level than at the proposal level.
for example, here, it's… this is very valuable, and we get… if we would have already implemented so that we do the processor on our side, and then eventually donate, as Elastic donates this enrichment processor, we now would have to go in First, do all of these changes to the existing implementation, but also impose breaking changes to all of our customers that have already used this processor. So I think this is a good example where we're getting a lot of value from this kind of discussion, and that informs the implementation at the start versus later. So… Yeah, take this as a point, yeah.
**Dmitrii Anoshin** 41:14 I definitely understand your point here, especially for something, like, widely… like, something that would… more users would be… benefit from, not just, like, some vendor-specific things. It kind of makes sense to at least run it by community, even if it's not being accepted. Eventually, at least you'll get some feedback to be more aligned with OpenTelemetry ecosystem.
**João Duarte** 41:38 Yep, agreed.
**Rob Bavey** 41:53 Yeah, thank you for that, appreciate it.
**Dmitrii Anoshin** 42:01 Should we go to the next topic? Trent?
Yes.
**Trent Vigar** 42:10 Hey, yeah, sure, thanks. So this one might be quick, and hopefully it's… it's just best suited for last, and it might even be better suited for Slack, since it's just a quick kind of question I've got about… a PR I've got open, but I'm just curious about the review process, and we've already touched on it a little bit here, about kind of, like, the… the SLA for approving workflows to run on a PR I've got open, and just… I've already got an approval on a PR, which I've linked in the agenda here on the Datadog receiver.
And I'm just waiting on the workflows to run, so, you know, I can get things merged and all that, so just curious about what you know, what the… what the process is. Like, if… if I keep having to merge main in, and then wait a couple days to run my workflows, I'm gonna be kind of endlessly looping, so just wondering what other people recommend.
**Dmitrii Anoshin** 43:10 And typically, it… we would wait for the API to be green, and assume that… contributor. So you're struggling with the fact that your pipeline has to be accepted first before it can even run. Is that the case?
**Trent Vigar** 43:29 just waiting on the workflows to… to run. I… they failed, when somebody approved them to run the first time.
And… then I pushed a change to fix it.
You know, to fix the reason that it failed, and they haven't run since, and You know, I also wasn't sure if, like, we're good to merge to main with a stale, you know, a branch that doesn't have latest main merged in, and in which case I keep having to merge main in every couple of hours as things get merged in, so I wasn't sure if I would keep having to wait, you know?
**Dmitrii Anoshin** 44:01 You don't need to merge main, as long as there are no conflicts. If you see conflicts with main, you would have to do it, but otherwise, you don't need to. You just need to ensure that the CI is green. Currently, it's not green. Currently, there are… the CI is failing, so we need to fix that.
about, accepting… accepting CI to run, it's, It's something that you have to go through, just as a first-time contributor. Once you push this PR, any other PR from your site would be automatically… would automatically trigger the CI?
So, yeah.
**Trent Vigar** 44:38 Okay.
**Dmitrii Anoshin** 44:39 First-time contributors is, like, challenge, like, Complicated to get.
**Trent Vigar** 44:45 And that's understandable, but okay. Well, that's helpful, that makes sense, and Yeah, I'll just keep a… keep a lookout on these when they run, and I think that answers my question.
**Dmitrii Anoshin** 44:56 Sometimes I even recommend people just, like, submitting, like, easy fix, something that they find in the codebase, like typo or something.
which can be quickly merged, and then it unblocks the CI for them going forward.
**Trent Vigar** 45:10 Yeah, that would be great. That's helpful.
**Jade Guiton** 45:13 So, for the record, like, there's a lot of the CI that you can run locally, that can be simpler sometimes than waiting for, than pushing, and waiting for someone to approve, and waiting for the CI to run. There are some things where it's not easy, like… Things that take a very long time to run, but if it's a localized change to a single component, often it can be… it can be done.
**Trent Vigar** 45:38 Right, yeah, I started to do that, yesterday, I think ACT is the tool I was using to run it locally, and there was some, like.
Kubernetes artifacts that are deep… deeply nested in the GitHub folder that it was unhappy about, and I probably could have just, you know, pointed at a specific workflow to run instead of, like, getting… waiting on the errors. But… Yeah, that's helpful.
**Jade Guiton** 46:02 Yeah, that's often the problem with contribib, like, if you try to run every test on everything, it's gonna take a really long time, and there might be breakages. So, yeah, I suggest, looking at the makefile commands for the specific component that you're working on.
**Trent Vigar** 46:20 Got it, yeah, that's helpful, thank you.
**Jade Guiton** 46:25 Also, yeah, I guess… Part of the problem seems here that we're wait… you're waiting for responses from the code owners.
Like, if you have… You might… try to, like, ping them on Slack or something, on the CNCF Slack.
Well, once… once the CI builds, I suppose it's better.
After… afterwards.
**Sam DeHaan** 46:51 Yeah, if you just need general, like, CI approval, just posting in OpenTelemetry dev will get you a relatively quick response for getting CI running.
**Trent Vigar** 47:02 Perfect. Yeah, thank you.
**Dmitrii Anoshin** 47:26 Sorry, go ahead, Dimitri. Yeah, I just want to say pretty much the same, that there are no more topics for today, so… If anyone else has something to discuss, feel free.
Otherwise, we can probably wrap it up.
Thank you, bro.
**Pablo Baeyens** 47:45 Right? See you on the internet. Bye.
