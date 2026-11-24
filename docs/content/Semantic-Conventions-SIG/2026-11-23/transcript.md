SIG: Semantic Conventions SIG
Date: 2026-11-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:55 Hello. Hi, Michele. How are you?
**Michele Mancioppi (Dash0 Inc.)** 00:59 Hi, how you doing? I understand that Josh and I were supposed to catch up today, but He is probably sick.
So he said he got a cold or something.
So I don't think to see him in the meeting today.
**Liudmila Molkova** 01:16 I don't expect to see him either, but he'll probably see Trask and maybe Christoph.
**Michele Mancioppi (Dash0 Inc.)** 01:23 Yeah, we were supposed to have fun about… Metric aggregations and why it is so hard for people.
And…
**Liudmila Molkova** 01:31 Dmm.
**Michele Mancioppi (Dash0 Inc.)** 01:32 I understand why he got sick.
The thought of it.
Doesn't make me happy either.
**Liudmila Molkova** 01:41 He got sick on Friday, so he was very sick from this discussion, you see.
Yes. For a long time.
let's see if we have Quorum today, I hope we should.
I am going to start presenting.
**Trask Stalnaker (Microsoft Corporation)** 02:15 Good morning.
**Liudmila Molkova** 02:17 Hello.
So, let's see what we have to chat about today… I wanted… to bring up a few topics. If anybody has, some additional topics, please add. Let's just spend a few minutes.
Nobody wants to talk about anything but me.
**Trask Stalnaker (Microsoft Corporation)** 04:33 Yeah, I was looking at my topic that carried over from last week, and you already have a… very clear reply to that, so I don't think we need to… Discuss that.
**Christophe Kamphaus** 04:46 I wanted to talk about the long-span events, but I don't have the proposal ready.
**Liudmila Molkova** 04:55 Since we have time, we can… Brainstorm if you want.
Okay, but we can… yeah, maybe we should add our names.
Okay, so Luis, how do you feel about starting with yours?
**Lewis Lewis** 05:25 If you want me to start, I will start.
Trask, thank you for leaving comments. There's a discussion Do you want to clear that up now, or stick to the comment thread?
**Trask Stalnaker (Microsoft Corporation)** 05:37 plan… I, we'll probably have to think about it and look up, Cause I got… I… got myself very confused, or I learned something about the app services, sort of the intersection of plans and instances, and what replicas, and, like, it's… Confusing, and so just trying to figure out how that maps.
**Lewis Lewis** 06:11 Yeah, it kind of is.
I think that Thompson's suggestion of just using the generic app service lets us… Sort of treat all of the different things in the way that they're not entirely related to each other, because none of them are entirely related to each other, really.
So I would probably go with that. But, we can do.
**Trask Stalnaker (Microsoft Corporation)** 06:36 representing.
**Lewis Lewis** 06:37 In the thread?
**Trask Stalnaker (Microsoft Corporation)** 06:38 The simple… so the proposal is in the simple name… Is the… instance is the plan… corresponds to the plan.
**Lewis Lewis** 06:53 The plan is a different thing.
So there's a thing called a stamp, there's a thing called a plan, and then there's an instance.
And none of them… and they sort of have a hierarchy, but they can also sort of move around between each other.
Especially when you're scaling and changing things.
Which is why I felt like… Having them each be their own object.
This one… this one is the… the instance.
**Michele Mancioppi (Dash0 Inc.)** 07:21 20 years.
**Lewis Lewis** 07:21 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 07:22 The instance.
**Lewis Lewis** 07:25 licenses are within plans?
So, we could… but we could also have a separate plan.
**Trask Stalnaker (Microsoft Corporation)** 07:35 Okay, so there is something called an instance, and that is the… Stamped.
Or what… what…
**Lewis Lewis** 07:42 No, the stamp is a… the stamp is a bigger thing. The stamp is, like, a collection of servers, I believe.
Okay.
**Trask Stalnaker (Microsoft Corporation)** 07:53 So… So it's the app…
**Lewis Lewis** 07:58 link. Is that the app?
**Trask Stalnaker (Microsoft Corporation)** 08:01 Oh.
You can have multiple.
**Lewis Lewis** 08:02 The app will have one plan, but it can have multiple instances.
And it's usually on one stamp, but considering they use the words usually, I'm guessing there's cases where it's not. Yeah, the diagrams are useful.
**Liudmila Molkova** 08:19 Which one of them? Or is there a better one?
**Lewis Lewis** 08:23 The one you were just looking at, I think… Yeah, so… Mmm… The one with the colors. Sorry, I don't… that's a very imprecise name.
Under workers.
Yes, this one.
Huh.
So… let's see… So this is sort of a depiction of a plan.
And… The plan has these workers. The first one… Is, an expansion of… the size N, which they've labeled in an interesting way. And the last one is an example of multiple… Buh.
I think it's supposed to be multiple plans within.
The… stamp.
But yeah, this is confusing.
So, your confusion is understandable.
**Trask Stalnaker (Microsoft Corporation)** 09:31 And each one of those little cloud box things is… is an instance, what we're calling an instance.
**Lewis Lewis** 09:38 Each one of those box things, I believe, is what we're calling an instance.
**Trask Stalnaker (Microsoft Corporation)** 09:43 Okay.
**Lewis Lewis** 09:43 And then they also use the word worker.
And, I've been thinking of the worker as the other instance ID.
Which I think is correct.
**Trask Stalnaker (Microsoft Corporation)** 09:54 as the other instance ID.
Other compared to… Yeah.
**Lewis Lewis** 10:00 So, you might remember from the beginning of this conversation, there's the machine name, which is used as the instance ID on the metric.
And there's the, service instance ID environment variable, which is used as the instance ID on the app logs.
And they're just both called the Instants because… I don't know, ask the people who made Azure.
I'm just working from the interface of documentation.
**Trask Stalnaker (Microsoft Corporation)** 10:38 Cool. Let me, that, that helps.
A bit. Let me… I will try to… Set aside some time today to re, re-acclimate, re… get that back into my brain, and… and… Give you, yeah.
Thanks for bringing this.
**Lewis Lewis** 11:03 Yeah, and if you want to find me on Slack or anything, I will do my best to help.
That's it for me.
**Liudmila Molkova** 11:14 Awesome.
Thank you. Thanks for pushing us through.
Okay, I don't see other topics, so I am going to… Talk about a few things.
I want us to have agreement on.
So, we just released the… First, schema V2 GenAI for GenAI, and we have a PR for Semantic Conventions.
Then the interesting question is, how do we make up until this Gen AI dogs show up on the… Hotela, your website.
And… There was… there was a good discussion.
for… the layout?
I think this one… And we settled somewhere around this option.
I think so, at least?
So… We would have Semantic Conventions as a folder, And then we would have… The siblings, the core for the central repo, and then the links for all the federated repos.
And, this is the… mock-up of this. Well, not the mock-up, but the… Implementation, the first one, the draft.
So this is the Semantic Convention folder.
Looks like it's all… it's in the same place.
And then there is the core.
I wish we could find a better name for this, actually, but we'll see.
So there is the core.
The GenAI links are gone from here, but only because… They just happened to be in the… In the same URL, but not in the same, group over here.
So all the old links still work, but they point to the new repo.
Yeah, so… nothing under… Changes, for now.
But the general layout does.
If we're good with it.
**Trask Stalnaker (Microsoft Corporation)** 13:55 The link… I mean, the URLs for the core stuff doesn't change. What's the URLs look like for the GenAI stuff?
**Liudmila Molkova** 14:07 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 14:08 Oh, just if you click on one of them.
Oh, yeah.
**Liudmila Molkova** 14:12 Give me a sec. You'll need to see how they were, and how they are.
Well, they could be.
**Christophe Kamphaus** 14:23 Yeah, the URLs, that was one of the reasons When we saw the boat.
Keeping Semantic Conventions score at the top.
But if the URLs are stable in this layout.
And I think it's fine, perfect in this structure.
**Liudmila Molkova** 14:40 Oh, they are not stable, but for the core, they change, but the redirects still work.
The… we configure this draft configures for directs from what they were to what they… are here. So let's say the database, Cassandra. So this is the new link.
**Trask Stalnaker (Microsoft Corporation)** 15:01 Oh, okay, so there is core in that, okay.
**Liudmila Molkova** 15:03 Yeah.
And…
**Trask Stalnaker (Microsoft Corporation)** 15:05 Gen AI.
**Liudmila Molkova** 15:08 And for Gen AI, because there is GenAI here, This link doesn't change.
So, it's… it's, it works already.
**Trask Stalnaker (Microsoft Corporation)** 15:23 I see. Okay.
Mcp would change, though, it would be under Gen AI now.
**Liudmila Molkova** 15:31 Oh, right. Yes, you're right. Huh, okay. Thanks for being my beta tester.
**Trask Stalnaker (Microsoft Corporation)** 15:37 It's okay.
**Liudmila Molkova** 15:50 Yeah, and… This one should still work.
Just redirect, yes.
So… What I'm looking from you is… support here, because I think it's missing SIG approval.
So, if we are happy with this layout, I want maintainers to approve, and this helps us move forward with Italia people.
To be fair, I, didn't get any feedback from them so far. I posted on the channel, but I think Patrice is on vacation.
And he would be the one to have a say in this.
**Trask Stalnaker (Microsoft Corporation)** 16:42 Do we need the URL to include CORE?
**Liudmila Molkova** 16:49 Oh, good question.
**Christophe Kamphaus** 16:56 What would you use instead?
**Trask Stalnaker (Microsoft Corporation)** 17:01 Just go straight to DB.
Because we wouldn't… we're not going to have conflicts there.
Anyway, given that these are just The namespaces should… Shouldn't come… the namespaces of any of these federated things shouldn't conflict with anything that's in core.
**Liudmila Molkova** 17:40 There might be some, because we have deprecated things.
For now. But we can… like, patch manually, right? We… I think we can work around it once.
And it should never happen again.
**Trask Stalnaker (Microsoft Corporation)** 17:55 What do you mean? How would you work around that?
**Liudmila Molkova** 17:58 We have a clear winner, right, the new thing.
And, we just need to configure it in AutelIO in some way. They have some manual workarounds for, let's say, broken links or something.
So we would explicitly say point there.
**Trask Stalnaker (Microsoft Corporation)** 18:18 It's not that important. I mean, I think… Being simpler, Mechanically, is… Probably better. I was just thinking if there wasn't any conflicts or problems.
It could be less of a… Change, for now.
And we wouldn't encode core. Like, I think you say the word core, like, is if there's a better name.
**Liudmila Molkova** 18:48 Yeah. Well, I'll check if I can get rid of the square. The… it would still appear here, though.
So, we can repeat Semantic Conventions core here, or we can…
**Trask Stalnaker (Microsoft Corporation)** 19:07 And call it basics.
**Christophe Kamphaus** 19:09 Maine.
**Liudmila Molkova** 19:13 Well, yeah, I mean…
**Christophe Kamphaus** 19:16 comments.
**Liudmila Molkova** 19:17 branch name.
**Rüdiger Schulze (International Business Machines Corporation)** 19:19 Actually, bass, like, I think it was used before, isn't it?
**Liudmila Molkova** 19:26 Not sure.
**Michele Mancioppi (Dash0 Inc.)** 19:29 I honestly don't think anybody would understand something like main bays or something.
It might make sense… To, break out… the, the families.
like… It's like to list out HTTP database messaging to make them easier to find.
There are many.
But I am skeptical that if we go and start Including on this page.
Using the same granularity as the different repositories that people break out.
It'll ever make sense for anybody outside.
The people working on it.
It's too obscure.
**Liudmila Molkova** 20:15 I think you're saying there are too many things here.
**Michele Mancioppi (Dash0 Inc.)** 20:18 No, I mean, there are many, right? But… Ultimately, what this page wants to be is a search engine.
Not a list of links, because now that we splinter out.
different repositories. Listing those repositories here is an implementation detail that nobody should care about, and I don't think anybody would understand.
**Liudmila Molkova** 20:44 I think we wanted this because they are versioned differently.
And…
**Michele Mancioppi (Dash0 Inc.)** 20:50 But the version and the origin repository is something that matters for the namespace, not on this list.
**Christophe Kamphaus** 20:59 There was a proposal to combine all of them.
But then, it might become very difficult if… Whatever reason, we have a conflict somewhere.
**Michele Mancioppi (Dash0 Inc.)** 21:11 Now, think about it.
In the federation, we say that no two repositories can declare stuff in the same namespace.
Right?
At least, that is what I know.
Which means every namespace has a repository and a versioning history.
Yep.
Which means the information of this namespace comes from that, and this is the version, is something at the level of the namespace, not that kind of list of repositories.
The list of repositories that we're making very prominent here It's no longer so interesting.
It's a detail, now, of where you find the Weaver model.
So if you want, if we want to make this as… Like, on that page, the list of repositories that somehow define semantic that we… that we blast in OpenTelemetry as official.
fine, but I doubt it's, it's too useful for end users.
And that page is very much meant for end users, in my opinion.
**Trask Stalnaker (Microsoft Corporation)** 22:31 The interesting idea about the version, whether the version is really that Relevant, or… or needs to be prominent there.
What?
**Michele Mancioppi (Dash0 Inc.)** 22:42 It is pretty relevant, because of the migration schema, right?
So, the version is really cool, but it's only insofar as a comparison between what you're using And what is the latest?
In case you want to use the schema processor.
In the collector to automatically upgrade.
**Liudmila Molkova** 23:06 No, it can include Jim or your… go ahead.
**Trask Stalnaker (Microsoft Corporation)** 23:09 Go ahead.
**Liudmila Molkova** 23:11 We could find a way to include schema URL in the signal, template. There is enough stuff there, so schema URL would be useful and wouldn't change much.
**Michele Mancioppi (Dash0 Inc.)** 23:24 I mean, not too bad.
**Trask Stalnaker (Microsoft Corporation)** 23:25 How is this?
Thinking from the doc perspective, like, we don't… if we encoded the schema URL, I mean, the version into the URL itself, then it would feel to me more like reference documents that, Are, you know, version encoded.
But all we're doing is kind of throwing that into the… Into the display.
I'm trying to think of the different users of, like.
Michele, you're… you're kind of making the… Distinction of the users of this page, of the doc site, Versus users… of… going directly to the repos, or directly to the Weaver models.
**Michele Mancioppi (Dash0 Inc.)** 24:24 So, for me, most of OpenTelemetry AO, most of it.
He's not for us.
In the 6.
It's for everybody else.
So whenever we present information in there, it should be directed to end-user adopters.
And as an end-user adopter, I honestly don't care which repository.
Gives me a semantic convention I care about.
I care only how it looks like, and how it looked like in the past, because the problem of migrating between attributes. That's why I'm saying, hey, let's not make so prominent the fact that we federated across multiple repositories.
And let's just put it on, on the single namespaces, so that people can go and fetch the Weaver model, and for example, plug it on their end.
In Weaver and in their observability pipelines.
Is that… Semantic?
That main page… wants to be a search engine of, hey, I would like to describe X, what should I use?
Do we want to plug in another lamb in there? Probably not. But maybe Jav with an enumeration of the possible namespaces or attributes, I don't know. But that is what I would expect on that page. Like, hey, Semantic Conventions, what are they? And which ones do I care about?
And then for the details, I go on the side panel.
**Trask Stalnaker (Microsoft Corporation)** 25:59 So that… I feel like that brings up, possibly, an even bigger… Question here of, You're saying that it's not meant for us, it's meant for other people.
But I would… Say that, like.
Most of the stuff under the spec?
section… Is not really for end users.
**Michele Mancioppi (Dash0 Inc.)** 26:30 Man…
**Trask Stalnaker (Microsoft Corporation)** 26:30 I mean, it's pretty…
**Michele Mancioppi (Dash0 Inc.)** 26:32 Well… It's not.
**Trask Stalnaker (Microsoft Corporation)** 26:34 Not like… it's not framed as user documentation, for sure, the spec repo…
**Michele Mancioppi (Dash0 Inc.)** 26:40 It is, that's the point. So, the spec repos.
I'm fine with that, but we put them in the wrong place. We gave them too much.
relevance. It's on the main page, Of the Semantic Conventions.
It's occupying the primest of real estates on that page.
Which implies that we consider it the most important.
And my point is, that's not the case.
You want to make a list of repositories and, like, fantastic Semantic Conventions and where to find them. Great. But it's at the end.
Oh, the navigation bar is something from experts to experts.
**Trask Stalnaker (Microsoft Corporation)** 27:25 Ludmila, I think, or… Christophe, I think you mentioned there was a proposal earlier to do that?
Do you remember what…
**Christophe Kamphaus** 27:42 Yeah, it's here.
**Trask Stalnaker (Microsoft Corporation)** 27:43 thoughts were?
**Christophe Kamphaus** 27:49 I think… Here, here.
I think it's this one.
It tries to combine them.
Now, also your comments there, we discussed it in this meeting.
**Liudmila Molkova** 28:32 Well, it's… okay.
So, if we did…
**Trask Stalnaker (Microsoft Corporation)** 28:39 Well, I think that one had registry, had the whole thing…
**Liudmila Molkova** 28:44 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 28:45 Sorry, go ahead.
**Liudmila Molkova** 28:46 So if we did this, it would be… Let's see… server…
**Trask Stalnaker (Microsoft Corporation)** 29:07 HTTP…
**Liudmila Molkova** 29:28 And then under, there would be attributes.
**Trask Stalnaker (Microsoft Corporation)** 29:42 So we would have MCP would be top level here, and then… I think.
**Liudmila Molkova** 29:48 Yes.
Probably you would need to include the full schema URL.
the family.
**Trask Stalnaker (Microsoft Corporation)** 29:58 Why?
**Liudmila Molkova** 30:01 Oh, otherwise, it's just that the only distinction is the version.
Or maybe that's the point.
Anyway, that's MITRE, we probably can, yeah.
**Michele Mancioppi (Dash0 Inc.)** 30:12 If I understand correctly this comment, this is what, It's the idea of putting it on the main content panel.
Of the Semantic Convention entry point.
**Liudmila Molkova** 30:28 Yeah, so this is the proposal, how I understood your proposal, that…
**Michele Mancioppi (Dash0 Inc.)** 30:32 It was actually a bit different. Not… so this thing here… We technically have it on the navigation bar, right?
What I think we should put on that page is a way to search.
For Semantic Conventions. Not listing them again.
**Liudmila Molkova** 30:53 We agree with you, but it's like, we still need to list them. So we should do search, too.
We do have…
**Christophe Kamphaus** 31:00 AI search.
**Liudmila Molkova** 31:04 I mean, we can do the proper search, that is… From Semantic Conventions only, because this one is across all open telemetry repos.
**Michele Mancioppi (Dash0 Inc.)** 31:13 It is… it is very noisy. Half of the time, I end up on the wrong thing.
And I search for Semantic Conventions a lot, so I'm a bit biased on that.
**Liudmila Molkova** 31:25 You know Bever has MCP server, and the search command, anyway.
**Trask Stalnaker (Microsoft Corporation)** 31:31 Can we put the… I mean, there's problems we… Can defer, such as, like, the search piece.
And there's problems we have to solve here, which is… the nav… What's the current… I mean, currently on that page, is there anything… Let's see… Oh, okay, there is a big list of everything. Okay, so that would continue to… we would… Oh, no, it's curated, I see.
Yo.
**Christophe Kamphaus** 32:11 It's not all namespaces.
**Trask Stalnaker (Microsoft Corporation)** 32:17 Okay, and so that could continue to be curated there.
**Michele Mancioppi (Dash0 Inc.)** 32:21 By the way, Liudmila, can you please click on any of them?
How do I know?
In which repository will I find the Weaver bundle for this?
**Liudmila Molkova** 32:35 Yeah, that's a good point, I should include it somewhere here.
**Christophe Kamphaus** 32:51 Yeah, if we combine them, we should also know where to edit this page, the model YAML.
Same report.
**Trask Stalnaker (Microsoft Corporation)** 33:04 Yeah, I like the version there. I'm kind of wondering if we really need the version in the navigation bar?
That feels like it's gonna be…
**Christophe Kamphaus** 33:16 I think it's a bit too much.
**Michele Mancioppi (Dash0 Inc.)** 33:18 Because that brings me neatly to my next point.
So, if we don't want… So I agree, the version there is confusing as hell.
Liudmila, can you please click on, one of the entries?
**Liudmila Molkova** 33:34 Like this, I clicked.
**Michele Mancioppi (Dash0 Inc.)** 33:37 So, in a world, like any of the new spaces, yes.
**Liudmila Molkova** 33:41 Oh, sorry, cloud… collaborators, okay.
**Michele Mancioppi (Dash0 Inc.)** 33:44 That sounds good. So, Trask is perfectly correct. Let's remove the version from here.
So that 1.45.0 in the breadcrumb would go away. Because as a user, That confuses me like that.
But the moment that that history goes away, you know what we need to add immediately, The version history.
So from here, I should have a way to see how they changed over time.
And that is the number one question that people that are in the journey of adopting Semantic Conventions on their own need to answer.
Good.
**Liudmila Molkova** 34:24 We don't…
**Christophe Kamphaus** 34:25 said, currently.
**Michele Mancioppi (Dash0 Inc.)** 34:29 I'm sorry, what? Yeah.
**Christophe Kamphaus** 34:31 We don't have it currently on the website, we need to go to the repository for that.
**Michele Mancioppi (Dash0 Inc.)** 34:36 Yes, and it's terribly complex.
As I know.
Thank you for my experience.
**Liudmila Molkova** 34:42 let's say there is a version history, so, like, I see the, I don't know, the span or something?
And what would version history tell?
**Michele Mancioppi (Dash0 Inc.)** 34:53 Comparison.
What it should tell us a comparison? What changed between these two versions? As a Git diff, or something very similar?
This went away, this got renamed. That would be amazing user experience. That would actually explain how they evolved over time.
**Liudmila Molkova** 35:10 Do… do we need it in Markdown, though, or not LAO? We… I think it's super useful, but, like, at this point, you'd rather look into something formally defined in YAML than, like, the different YAML.
**Michele Mancioppi (Dash0 Inc.)** 35:24 I profoundly disagree.
the, For example, it takes a significant amount of literacy in all things OpenTelemetry to be able to interpret the default Weaver model.
But as a user, if I hear from my vendor that, hey, actually, you know, it should not be, you should use htpresponse.co instead of HCP.
Status underscore code, And then in the diff, you see, okay, it changed from version blah to blah.
Then, you're seeing there, for example, also changes with the type, and all the other things.
And that is actually going to be a much more understandable metamodel. Most people Should never have to look at a Weaver model.
99% of the users should never have to do that.
**Liudmila Molkova** 36:14 Yeah, because they should do it with their agent.
**Trask Stalnaker (Microsoft Corporation)** 36:18 I think this is… I mean, this is… I like the idea, but I want to unblock Ludmila's kind of concrete work here, and I feel like that, you know, adding… adding new stuff is something we can defer from, you know, that doesn't need to block her work.
**Michele Mancioppi (Dash0 Inc.)** 36:38 I did not mean it as blocking her work. I thought it would make sense to rethink what we present and how to be more… and yeah.
**Trask Stalnaker (Microsoft Corporation)** 36:48 Yeah, yeah, I mean, I think it's a good…
**Liudmila Molkova** 36:49 super useful.
**Trask Stalnaker (Microsoft Corporation)** 36:50 Yeah.
Good discussion, I'm just, want to make sure that we… I'm hoping by the end of this meeting we can… unblock Liudmila from… at least so she knows what She's gonna work on… Next, without… At least… Separating what we think needs to be done here, now.
**Michele Mancioppi (Dash0 Inc.)** 37:18 Then I can often… the smallest delta, and that would be, putting on top of each namespace, like when you go in a Santic Convention, where it comes from, which repo, and then really treat the entry point as the list of repos.
Like, Semantic Conventions showing this website are defined in these things, and then find out which one is which, you need to go to a specific namespace.
That is probably the easiest thing to… to unclutter the UI and providing value.
**Trask Stalnaker (Microsoft Corporation)** 37:51 So, so, explain that, Because that sounds like the… more like what Ludmila has… Currently, which is first the repo, and then the conventions inside that repo.
**Michele Mancioppi (Dash0 Inc.)** 38:06 Yes.
**Trask Stalnaker (Microsoft Corporation)** 38:08 But I thought… I guess maybe Liudmila and I both misunderstood your…
**Michele Mancioppi (Dash0 Inc.)** 38:13 Oh, no, the Trask understood perfectly well. It's just me saying, okay, if we want to make the minimum delta.
what would provide value to the users is what Liudmila proposed.
with, that is, like, the smallest thing. I just… my entire point in the discussion was to point out that was… Far from, the, end state.
with the users in point of view. That's it.
**Liudmila Molkova** 38:40 I can… I can see how this is useful, so…
**Michele Mancioppi (Dash0 Inc.)** 38:48 Especially if we can make it as something that expands.
So by a collapsed thing with an accordion?
And somehow you can search in that list. So it's HTTP, or it comes from the general repo.
What is it called, right, Paul?
**Liudmila Molkova** 39:06 Yeah,
**Trask Stalnaker (Microsoft Corporation)** 39:08 I'm trying to separate the, like, rearrange, like, what we want to establish here is… The navigation bar format, and we can kind of, you know, pick any rearrangement we think is best there.
And, you know, the basic layout.
I don't think that… none of that is a lot of work if we just decide what we want it to be.
But then adding searches and version histories and that sort of thing is… is…
**Michele Mancioppi (Dash0 Inc.)** 39:43 I…
**Christophe Kamphaus** 39:44 I guess it's a shared component.
the navigation sidebar, I mean.
So, adding a third feature to that one would probably… Oh, yep.
**Liudmila Molkova** 40:00 That's happening.
It's an additional feature. I think, like, let's try to focus on the layout. Yeah, agreed. And I'll document that the search is indeed a useful thing to have there. It's just, like… Yep.
**Trask Stalnaker (Microsoft Corporation)** 40:17 But Michele, aside from searching… What is sort of… what… I just wanted to, as a… as a power user of this… these pages, what is… what do you see as the ideal navigation now bar layout.
**Michele Mancioppi (Dash0 Inc.)** 40:37 I think we are mixing two aspects in this discussion. One is the navigation bar, and the other is the main page.
So…
**Liudmila Molkova** 40:46 The main page is… is what?
**Michele Mancioppi (Dash0 Inc.)** 40:49 Go to click this.
Oh, the, the one, yes.
No, we had the one with the registries. Okay, let's say… let's say this one, right?
So, in here.
**Trask Stalnaker (Microsoft Corporation)** 41:04 Oh, do you mean in Ludmila's PR?
**Michele Mancioppi (Dash0 Inc.)** 41:07 Yes, exactly. Because that is what I was arguing about.
**Trask Stalnaker (Microsoft Corporation)** 41:10 Can you…
**Liudmila Molkova** 41:11 Oh.
**Trask Stalnaker (Microsoft Corporation)** 41:13 Yeah, this… this guy.
**Liudmila Molkova** 41:17 Oh, I don't know why, but…
**Michele Mancioppi (Dash0 Inc.)** 41:20 Yes.
So, here, the navigation bar, on the left-hand side.
I don't think we need to expose Core or Gen AI. I think there we should keep the structure as we have it today, and hide away the versions, because that is confusing.
We can show the versions.
Inside each namespace, like, latest version is blah.
see the history linked to the repo for now, okay? Defined in there, see the history linked to the repo. Cool.
So, the main navigation bar remains the current flat list of namespaces, which actually is quite discoverable, long but discoverable, and we removed the concept of version from there, because that is confusing the SAC.
And I do not like particularly, the… so, that's for the navigation bar for the main page.
This one, I don't think it's very end-user orientated, it's more like, these are the repos and where you find them.
Okay?
**Trask Stalnaker (Microsoft Corporation)** 42:31 So more like the old… the existing website.
So basically, maintain the… you're suggesting to maintain the existing website.
**Michele Mancioppi (Dash0 Inc.)** 42:40 Struck.
**Trask Stalnaker (Microsoft Corporation)** 42:40 sure.
**Michele Mancioppi (Dash0 Inc.)** 42:42 I don't like that one.
Too much other, because it's the repetition of the main navigation bar.
And I… This is exactly a subset of the main navigation bar. A very, very large subset.
**Trask Stalnaker (Microsoft Corporation)** 42:55 You know what I mean?
Sorry, I… that I'm not understanding.
**Michele Mancioppi (Dash0 Inc.)** 43:04 The content that you see on the, on the main, the main panel.
**Trask Stalnaker (Microsoft Corporation)** 43:08 Oh, the nav. Oh… And that the page here is the same as the navbar.
**Michele Mancioppi (Dash0 Inc.)** 43:14 It's very… it's too similar, right?
**Trask Stalnaker (Microsoft Corporation)** 43:16 Okay.
**Michele Mancioppi (Dash0 Inc.)** 43:17 So, of course, I mean, I expressed my opinion that this should be a very good search.
**Trask Stalnaker (Microsoft Corporation)** 43:24 Right, right.
**Michele Mancioppi (Dash0 Inc.)** 43:25 You said, yes, but that's a bit too much work, and I agree with you.
So then the question becomes, okay, what useful things Can we put on this page?
**Trask Stalnaker (Microsoft Corporation)** 43:35 Okay.
**Michele Mancioppi (Dash0 Inc.)** 43:37 I have a few ideas for that.
the PR on Ludmila is listed in the repositories.
There is usefulness in that.
**Liudmila Molkova** 43:48 Yeah, I'm happy to change it.
**Michele Mancioppi (Dash0 Inc.)** 43:52 No, but…
**Liudmila Molkova** 43:52 If we have specific proposal, let's go first.
**Michele Mancioppi (Dash0 Inc.)** 43:55 it, I speak with a lot of end users, yeah?
And, when they talk about semantic conventions.
One of the questions they have is.
Which ones are advanced vital, and we discussed about this with versions and history and everything else, cool. You know what is the second question that comes, at least from the more refined ones, is, how do I make my own?
So, we could use that content To explain that these semantic conventions are done with Weaver.
And this is how you can make your own.
Because it's… So, more talking.
**Trask Stalnaker (Microsoft Corporation)** 44:37 about what's… so more targeting, hey, this is… this is what Semantic Conventions are, this is how to use them, this is how to build them, that… Yes. Sort of.
Like, a high level.
**Michele Mancioppi (Dash0 Inc.)** 44:50 What are they good for? Why are they important?
You know, that is the entry point of Semantic Conventions. Why do they exist?
Why are they good for your health?
And how can you roll your own?
Because that would be an excellent entry point for people to discover the magic of Weaver.
**Trask Stalnaker (Microsoft Corporation)** 45:24 So, I mean, Ludmila, I think, you know, that's still… you know, as far as going like-for-like, kind of the minimum transition, I think just, you know, the links there is what we have today.
you know, so that could be what we have.
you know, app in your PR…
**Liudmila Molkova** 45:45 I think this PR does not… oh, this PR, does it? Yes, it does touch it. It's the page that belongs in that PR.
Not in this, I'm conf. Okay.
**Trask Stalnaker (Microsoft Corporation)** 45:56 So, I mean, you could just re-flatten it back. Right now, I think you have the… just the small page of the links to the repos, but we could… Just kind of preserve.
Since we're talking about more preserving the existing structure, just my.
**Liudmila Molkova** 46:11 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 46:12 Version numbers, and moving the version numbers, and… and… repos… Into the page itself as sort of like a footer, almost.
**Liudmila Molkova** 46:25 Yeah, I'm thinking about this, and what… Michele says, and what we ended up with, I think brings the point of We need a place?
That formally combines soil registries?
Auto registries, because it is what it… it's what we're trying to model.
There's this discussion?
**Michele Mancioppi (Dash0 Inc.)** 46:46 That could be at the end of that, of that page.
**Liudmila Molkova** 46:51 Yeah, yeah.
So, one does not contradict another.
**Michele Mancioppi (Dash0 Inc.)** 46:55 Okay.
**Liudmila Molkova** 46:55 But, like, Autel Leo should not be the… owner of combined list of Semantic Conventions that should live somewhere in some conf, I think.
**Michele Mancioppi (Dash0 Inc.)** 47:08 Okay, you lost me here? What do you mean?
**Liudmila Molkova** 47:13 So… Today, Autel.io knows about these two repositories.
**Michele Mancioppi (Dash0 Inc.)** 47:21 Yeah.
**Liudmila Molkova** 47:22 This repository knows about itself. This repository knows about itself. Nothing knows about two of them.
**Michele Mancioppi (Dash0 Inc.)** 47:29 Agreed.
**Liudmila Molkova** 47:31 It's implementation detail.
But the implementation detail is to make the… Maybe only docs visible.
Uber repository that combines all… all of them. And this is what enforces the… Uniqueness of namespaces.
**Michele Mancioppi (Dash0 Inc.)** 47:55 So, I do not believe every user ever woke up in the morning and asked, I wonder how many repositories define semantic conventions that utter concerns officially…
**Liudmila Molkova** 48:05 I agree with you. Yeah.
**Michele Mancioppi (Dash0 Inc.)** 48:08 Then I do not understand the proposal anymore, I'm sorry.
**Liudmila Molkova** 48:11 It's not the proposal, it's the… that the proposal that we are making here, the combined list of repositories, and not exposing users to this complexity, for us, it means a newer Weaver repository is an implementation detail. Users don't need to know about it.
Maybe they will, if there is a platform release or something. This may be useful for the packaging.
But it's more interesting there.
**Michele Mancioppi (Dash0 Inc.)** 48:38 There is a potential subset of users that want to run validations against all the… with live check, against the official models, but for them, the place for that would be probably the Weaver documentation, or a paragraph in the first page.
**Liudmila Molkova** 48:58 Yeah, and this… the same thing is for us to make it right. I'll… I'll see what I can do without it. I think we would need to do this eventually.
But I don't want to block us.
today on this, so I'll see what I can do meaningful, and it sounds like… Is there anyone who would be… Strictly opposed to try out this organization.
Or I was just checking… in my mind, we kinda… Landed on this as an alternative proposal to the current.
And, like… would people want to try this one as well?
Okay.
Cool, so I'll maybe make another prototype, but we'll see how it works.
Thanks a lot, I've got a lot of useful feedback.
Thanks, Michele. How are you? We need your product voice here.
Yeah.
A couple of small ones.
So, here, I have a PR… I think, Chris, if you reviewed things.
So we can close… I don't remember what the discussion was, but it seems… We are fine.
**Christophe Kamphaus** 50:24 It was mainly to take some of the release checks that were part in Weaver, and to also do those.
And you, did some, so I'm fine with merging it as it is now.
**Liudmila Molkova** 50:39 Okay, cool. So then we don't need to talk about this… Really?
And… I hoped Josh would be here, but I wanted to talk about this repo.
So… So today, the maintainers of this repo are… beaver maintainers, It does not get… That much love, but also it affects, like, the common layout and policies that we have in Semantic Conventions.
So I wanna check how we would feel about having Semantic Conventions maintainer.
maintain it.
And it'll literally work, like… the… there are very few PRs. Not much is going on here, but, like, for example, Rudiger has a PR for the… How entity refinements and metric refinements would look like in the registry.
And essentially, this is something that Semantic Conventions maintainers should have a say in.
**Rüdiger Schulze (International Business Machines Corporation)** 52:01 Right, and it's especially about the format, and how you can navigate, and, you know, as we… I mean, this is an aspect where, again, these, you know, federated, Conventions, repo, and then cross-reference to the core or base come in.
And, It's actually good if you, you know… this goes also back to the user perspective, right? As a user, you… you… want to, for a certain entity, understand what are the… first of all, the attributes, what are the metrics, but some of the metrics, they are either defined in core or in your federated repo.
And anyway, as a user, you just want to be able to… Seamlessly navigate from, you know, these definitions independent of where they come from.
**Liudmila Molkova** 52:59 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 53:01 Amilla, could you give, kind of, because I have not… paid much attention to this. Could you kind of give an overview of… what the packages drive, is that, like, driving the dock generation, primarily?
the, like, Jinja templates, what… what kind of premier, I guess, oh, Rego policies, what all, what all… What all am I agreeing to maintain?
**Liudmila Molkova** 53:32 You don't need to agree. So yeah, the common policies that we actually already use in the core Semantic Conventions, and then GenAI, and everybody.
who is doing the federated Conventions should use a set of policies. So, for example, this is the stability ones.
This is the Rigo template… oh, sorry, Jinja templates for the markdown. We don't use them in GenAI or Core, but once we move… like, we could start using them in GenAI.
And once we move Semconf to V2, this is the templates I think we should be using there.
And the… eventually, it should have… the idea was that the code generation templates would go here.
So, like, the code generation templates for Python, Core, Sempontrepo, and GenAI would be the same, and they need a shared place, even if they are for this specific language.
Nothing stops, like, Python or whatever language to own their own, but, like, if you want to share it, especially with third-party users who want to define their own conventions, this is a good place to keep them shared.
**Trask Stalnaker (Microsoft Corporation)** 54:54 Cool.
**Rüdiger Schulze (International Business Machines Corporation)** 54:56 From a mainstay point of view, I can only concur, actually, we don't want to maintain them in our repo. We would like to use the shared one.
**Liudmila Molkova** 55:11 Okay, so I don't want to answer from you, I'll thoroughly post in the maintainer channels, and we can discuss where they are, or, like, you… you can share with your concerns.
**Trask Stalnaker (Microsoft Corporation)** 55:22 I have proof.
**Liudmila Molkova** 55:25 Okay.
Cool.
Thanks.
So we have 5 minutes. I don't think we can make a lot of progress, but let's see what we can do.
Since we can merge this front… Oh, it's resolved.
**Trask Stalnaker (Microsoft Corporation)** 55:54 It's already resolved. I know, I have all of la- all of the last, like, last week of getting used to this new UI.
But, like, how'd you.
**Liudmila Molkova** 56:03 You're right.
**Trask Stalnaker (Microsoft Corporation)** 56:03 all the brain cells. Like, I actually like… I mostly like it, I just… It's… I was so used to the existing one that it's just take… it's really hard to get used to such a revamp.
**Liudmila Molkova** 56:16 Absolutely, if you figure out how to just, apply changes from the suggestions in this view, let me know, because I couldn't find it.
Okay, a bunch is waiting on the reviewers.
And… Let's see… Oh, Christophe should have brought up this one.
So… Thanks for defining the writing documentation for metrics.
**Christophe Kamphaus** 56:51 Yeah, I think I've replied.
To your comments, sir?
**Liudmila Molkova** 56:57 Awesome.
Cool, so I'll take another look, and we'll get it merged.
Anything anybody wants to call out here?
Okay, I don't think anything's super controversial that we need to spend time on.
Then?
Thanks for coming!
See you next time.
**Christophe Kamphaus** 57:47 Thank you, see you all.
**Armin (Dynatrace)** 57:49 Bye-bye.
**Neil Yashinsky** 57:50 Thanks for your contributions and leadership to everyone. Have a good day. Bye.
