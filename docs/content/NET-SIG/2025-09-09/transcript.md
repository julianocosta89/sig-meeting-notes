SIG: .NET SIG
Date: 2025-09-09
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Zach Montoya** 01:08 Hey, Martin. How are you doing?
**Martin Costello** 01:11 Hey, I'm good, thanks. How are you?
**Zach Montoya** 01:13 Pretty good.
It's been cooling down in Seattle, so I'm very happy about that.
**Martin Costello** 01:22 It's a similar story here. It's getting… growing colder than wearing a hoodie now, rather than a t-shirt.
**Zach Montoya** 01:30 Yeah, it's a nice reprieve. It was… the summer is nice, and then it gets extremely hot, and then I wish for the clouds again.
**Martin Costello** 01:45 Hey, man.
**Matthew Hensley / Grafana Labs** 01:48 Hello!
**Alan West** 02:00 Hey, everybody.
**Martin Costello** 02:03 Hey.
**Zach Montoya** 02:04 Hello.
**Alan West** 02:09 Raj said he had a conflict today, so… I think, it'll just be us.
Oh, thanks. Somebody typed my name.
**Mike "Blanch" Blanchard** 02:31 I got you.
**Alan West** 02:34 Thanks, Mike.
Well, as usual, we got… Things for the agenda.
Plop them on there.
Otherwise… Are there any… PRs or issues people have on their mind that they'd like to chat through?
**Martin Costello** 03:40 I just, remind I'm still weighing on feedback.
For the issue description, for the… version harmonization.
thing for, all the NuGet package versions.
**Alan West** 03:55 Yes, sorry, I did read that last week, and then I think you're talking about this, right?
**Martin Costello** 04:01 Yeah, yeah, we don't have to go through it now, but yeah, I just thought I'd remind it.
**Alan West** 04:10 Yeah, I did read through it. I thought it looked pretty good. Though, sorry, I didn't, I didn't leave any comment, but I will do that.
But I think it describes the situation well, and effectively what we've agreed to, so… That's my take.
**Martin Costello** 04:32 Cool, thanks.
**Alan West** 04:43 Okay, I think, I think… Well, I don't have anything, so… Martin, I think you pinged me on something related to database stuff. Maybe we can just talk about.
**Martin Costello** 05:05 Oh, yes, there's, there's an issue you opened about 11 months ago to do with the stabilization.
And it's… to me, it looks like one of those sort of brain dump issues, where it's like, create… you get an idea out, and I'll come back to it later. But with no context, I'm not sure what you want to do with it.
**Alan West** 05:26 Yeah, it was probably, like, my thoughts at a moment in time.
And likely needs to be… Updated to reflect the current reality.
I think there's still something to this. I think I've kind of mentioned, This question on my mind, just this general question of… have… What should stability look like? How do we get to stable for… for entity framework?
Given that not all the database conventions are, are stable, Yet today. Like, I think, like, Oracle remains, Remains a holdout that's not yet declared stable, that of course you can use.
This instrumentation with Oracle, and of course there are… there are others.
That's just an example. But that's kind of what I meant by this issue, was just basically, devising a plan, what'll it look like? And I think we've kind of, like, spitballed some… some ideas, like the, Ability to somehow configure the instrumentation?
for certain… Data stores.
Or systems, DB systems. And, like, you know, having… having ones that are… don't yet have stable conventions, you know, having them be effectively, like, opt-ins. That's the… that's the… the type of thing that was on my mind in… in… in opening this issue.
**Martin Costello** 07:14 Right, okay, yeah, I hadn't… I hadn't thought of it in the context of… specific providers, I was just thinking of it like databases, because Other than the provider name, I don't think there's much in there that's… Specific to individual systems.
But I guess it depends, like, what lens you want to view it through, because if you treat… which database system is it as the primary key? Then that defines what the conventions are and if they're stable, but if you just look at it as, I'm a database.
Then it's a bit different.
**Alan West** 07:55 Yes.
That's kind of an interesting… If I'm… if I'm following you.
Like… Just coming to the conventions here, looking at the database conventions.
There… there are, of course, like, you know, super general conventions for metrics and spans.
That are kind of, whatever, database system agnostic. And then… There are slightly more specific conventions for things like just anything that's SQL-like.
And then… Going a step deeper down the rabbit hole, there are even, kind of, specific guidances for individual… systems like Postgres and MySQL, SQL Server is here.
And… I suppose… maybe… maybe this is what you were saying, but I suppose… If the thought is that an ORM like Entity Framework Was only beholden to, like, the most general conventions, and… say you were using Oracle, or MySQL, or Postgres, or whatever, that if there is anything Unique to these that they just would not be reflected in the telemetry produced by the instrumentation library.
That may be one… one path forward. Is that kind of what you were saying?
**Martin Costello** 09:40 Yeah, because, like, to be honest, only because I hadn't considered… the more specific option. I was just looking at it as the bare minimum option. But, I guess, like.
The bare minimum could be.
Go through everything it uses at the moment, compare that against the generic database conventions, and as long as it's not using anything unstable.
then that's, like, a bare minimum of stability, and then see if there's anything left over that's more specific. And then you could put something in the README that's, like, here are the providers we explicitly know about.
those aren't sta- if you view it in that… with that lens, they are not stabilized yet, but the general conventions are.
Because then, I guess, if you say they're not stable for the specific ones, then that gives you the wiggle room to go, oh, database provider X, everything we emit is stable, but we're not omitting the stable conventions for X, because A, B, and C are missing.
**Alan West** 10:48 Right.
**Martin Costello** 10:50 Or they've done, but not stable.
But I guess that creates a bit of a nightmare for the package version, because if any one is unstable, then the whole package is unstable.
**Alan West** 11:03 Right, and that's kind of where my mind was at in, like, basically making anything that is not yet stable being… Like, you have to explicitly turn it on via a feature flag that makes it clear that you're opting into an experimental feature or something like that, you know? Kind of like the pattern that we've used in… other contexts… One specific, just kind of, just kind of throwing a specific case at… the idea you were just expressing there is… my memory is getting jogged. So, db namespace is actually an interesting attribute.
in that… the… generic conventions let me just see what the most… going through this in real time, because I'm forgetting what the most recent verbiage is here.
But, so, db namespace, basically, blah blah blah, fully qualified.
Database name within blah blah blah.
Well, I think it has something… Yeah, semantic conventions for individual database systems should document what DB namespace means in the context of that system.
So… Basically, the conventions, the generic conventions here, are punting the, the… the convention or the definition of DB namespace.
to the more specific, thing, which differs depending on database systems. So, like, if we were to go to SQL Server.
And we were to look at… its definition of DB namespace, it takes into account, you know, some SQL Server-specific things, like instances, right? Like… some database… a lot of database systems have, like, a notion that's maybe similar to SQL Server's concept of an instance, but… the SQL Server conventions, I get very explicit about what DB namespace, how DB namespace should be constructed. It should literally be the string Instance name, if it's present.
Followed by a pipe.
Followed by the database name.
So, given that, you know, SQL Server conventions are stable.
That's cool, if you're using the… EF core.
instrumentation, and you identify that you're using this DB system, then… I… at least it would be… I'd expect that the… that… the instrumentation would construct the DB namespace based off of the rules articulated here.
Compare that to Oracle, which is… Still in development. So, subject to change.
it, Oracle has a slightly, different set of whatever concepts, It's just architected differently.
So… how DB namespace is constructed here is just different. So… I guess the thought in my mind was that the… EF core instrumentation would be smart enough to, like, you know, do the… do the right logic, based off of… The system name.
**Martin Costello** 14:55 Right? So… all that sounds to me like EFCore's missing a bunch of infrastructure to deal with, How does it do database-specific?
Resource attribute overrides.
Like, we've added a bunch of stuff into it recently for… the new conventions.
But there's… other than devolving into a giant if-else, web.
There's… there's no… there's nothing built into it to sensibly have it fork off and change the meaning of specific attributes.
just spitballing off the top of my head. Maybe it needs something similar to, but not the same as… the stuff that's in the AWS… instrumentation that deals with the different, Atlantic Convention versions.
So, like, once you've determined which system it is, then you can go off and go, oh, if it's Oracle, run these extra rules to override stuff. If it's SQL, do this. That doesn't answer the question about stability, but it feels like there's a bunch of missing… Boilerplate inside it to deal with all of that.
**Alan West** 16:22 Yeah.
Yeah, I don't know what the answer should be off, like, right offhand. You mentioned, like, the AWS approach, Which is interesting. I have pondered whether… That… Could be applicable to… Other instrumentation, or an approach for us to, you know, drive other things to stability.
It has some drawbacks, though.
In that… We're basically… that AWS instrumentation, it's… At the point that we went stable with it.
It was pinned to a specific version of the conventions, which… you know, is no longer the current version of the conventions. And so that default is… Kind of set in stone until the day that We decide to basically do a major version bump of that instrumentation.
**Martin Costello** 17:40 I was thinking more on… along the lines of… Less that it's to do with the convention versions, and more… How do you override the value of a specific attribute.
If you're this, I did BMS over that, or DFMS.
Because that would then maybe tie into the comment in that PR last week.
about, oh, if someone comes up with their own custom EF provider that doesn't have anything specific, there's no way to, like, plug in to it?
You could, of course, just use the enrichment and hook it all in there.
But, there isn't, like, a first class… I'm a different… I'm database system X, customize stuff for that.
**Alan West** 18:39 Right.
And at least for our purposes, Enrich is not really, like, a great… Enrich is something that, like, you know, an end user would use versus, you know, us as instrumentation authors.
**Martin Costello** 19:00 I think there's an… we've… there's enough context to come out of this discussion.
that I think I could go away and… Look into all the different specific conventions and see what the current state is.
because we.
**Alan West** 19:19 Okay.
**Martin Costello** 19:20 We could… because we could potentially… at the point that SQL Client is stable.
we could potentially still not ship EF Core as stable then.
But ship it at the same time, so all the… like, the… the big overlap on the Venn diagram of the database conventions is the same as they are for SQL Server.
So that at least those two are in step with each other.
**Alan West** 19:47 Yeah, totally. Yeah, I like that.
Yeah, okay, anyways, I think… That's what this issue was about, primarily. So… Yeah, if you want to keep on thinking about that, if you have some good ideas… That'd be cool.
**Martin Costello** 20:23 I'll do some research on what The state is, and then maybe have a think about doing, like, a prototype to throw away of what we could potentially do.
**Alan West** 20:37 Okay.
Yeah, and you know, largely, I think that… I think that the… the differences across the systems… I don't think that there's… a lot. I think that there's more overlap than not. You know, I… there might be a few more things than what I've noted here.
But… at least at the point in time that I wrote this issue, these were the things that, are… We're called out as basically… Defer to the more specific inventions to figure out what you should do with these attributes, was basically the… the… the thing. So… Again, there might be a couple of other things, I could probably take a pass myself, it's been a little while, but… Again, I think it's mostly… uniform across.
At least the sequel-like.
systems.
**Matthew Hensley / Grafana Labs** 21:37 Somewhere to… if you want to talk about, like, hey, you can't use Enrich necessarily for these.
Our friends over in Java Land have customizers all over the place that are pretty baked into that ecosystem.
And so you can ship, like, an instrumentation package with a customizer and… Control things, like how to define the namespace attribute, and override the defaults.
**Alan West** 22:08 Yeah, so if we were to apply, like, an architecture like that to, this circumstance, like, what would you think that that would look like? Would it be, like, a… An end user would obviously take a dependency on the… On the instrumentation library, and then… Would it be your vision that it would be on them to… know, of course, what database systems they're using, and then if we had the concept of, like, a customizer, whatever that would look like for us, they would also take a dependency on that, and then… Like, magic would happen.
**Matthew Hensley / Grafana Labs** 22:44 Yeah, just, that's kind of what they do with the Java agent and bundling a lot of things. But just as an option, they kind of have plugins all over the place, where we have the enriched callbacks.
**Alan West** 23:01 Yeah.
Yeah, we could certainly, like, have, have, like, a database system-specific, package that… You could take a dependency on that bundles with it, like, a specific enrich.
Carl, which… actually doesn't cover everything, right? That's only traces, right? It wouldn't affect anything on metrics.
But… the concept, something like that.
Might be… might be something to consider, yeah.
**Matthew Hensley / Grafana Labs** 23:44 Just wanted to share that there's prior art here, even though it's not necessarily idiomatic.net. I think it's pretty typical in Java.
To have this stuff.
**Alan West** 24:04 Yeah, okay.
That's all I got.
Anyone else?
**Martin Costello** 24:19 I'll let… I'm just gonna quickly mention it, but it was Raj who brought it up originally, and he's not here. Rc1 of .NET 10 came out a couple of hours ago.
So, I've updated the two PRs that are open in draft.
for the updates for that, but I'm not sure what the next step on that is, because Raj made it sound like To merge those and have a… do a release candidate soon.
But yeah, I just thought I'd point out that, like, that's now happened.
**Alan West** 24:54 Okay.
Yeah, I can ping him and see… see what… Plans he… Has in mind for that.
He's around today, so I just… I think he just wasn't able to make it to this meeting.
Cool.
Alright, y'all.
See you next week?
**Martin Costello** 25:24 Bye.
