SIG: Semantic Convention Tooling
Date: 2026-09-30
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth (Google LLC)** 00:45 Hey!
**Jeremy Blythe** 00:52 Hello.
**Josh Suereth (Google LLC)** 00:54 How are you doing?
**Jeremy Blythe** 00:55 I'm good, how are you?
**Josh Suereth (Google LLC)** 00:58 Oh, alright.
Yeah.
**Jeremy Blythe** 01:01 Oh.
I wasn't very confident.
**Josh Suereth (Google LLC)** 01:05 Yeah, it's been, work has been really stressful, but we're good.
**Jeremy Blythe** 01:11 like.
**Josh Suereth (Google LLC)** 01:11 Lots and lots and lots of stuff going on.
**Jeremy Blythe** 01:14 You know, it's been busy.
**Josh Suereth (Google LLC)** 01:17 What?
**Jeremy Blythe** 01:18 Let's be busy.
**Josh Suereth (Google LLC)** 01:20 I that that's true. I'd rather be busy than not busy.
**Jeremy Blythe** 01:23 No.
**Josh Suereth (Google LLC)** 01:26 Yeah, it does mean I haven't had enough time to pay attention to all the things I need to pay attention to.
But we're getting there.
This is one… I was reviewing this, and this is, This one has me nervous, man.
This PR.
**Jeremy Blythe** 01:46 How's you nervous?
**Josh Suereth (Google LLC)** 01:55 Is it… so, template types…
**Jeremy Blythe** 02:01 So.
Rewind 2 years.
When I first started working on Weaver with you guys.
Yeah. Started putting Life Check in, and we had a discussion Because I was baking in things that were, that were hotel-ish.
And there was, we had a bit of a debate about it, and I think Laurent was saying.
Oh, well, it… Weaver's specifically built to be, like, agnostic, so it doesn't, like, to have all the hotelisms.
And one of those hotelisms is the fact that we have namespaces separated by Full stops.
And so I took. I deliberately took code out.
That was in there.
that hard-coded dot as the separator, and, you know, and we move that deliberately into RIGO policies.
Which was which was a great decision.
because then that meant that we had the ability to extend live check into Rigo and all of that. But what There was, like, this fundamental principle which was to actually shift the hotelisms so they weren't, like, baked into Weaver, and I think Over time.
what we've done. And you know, with, if you look at like Liudmila's search.
Hello! Perfect timing.
It's like I summoned you.
you.
**Liudmila Molkova** 03:34 the.
**Jeremy Blythe** 03:35 If you look at the research there, we've… we have, like.
We have kind of drifted to embed the… Otelisms more and more into Weaver.
So this namespace separator was my attempt at going, well, maybe we shouldn't be doing that.
Really, what the… really what the Pr is about is about fixing that bug that came up where it was doing a naive sort of starts with.
where it should be using starts with O and the… and… and you need a separator before you do the key part of a template type.
matching.
So it's… it's like a super simple fix.
to a silly bug.
But it took me back to… That initial discussion… One of the very early discussions, which was Yeah, but we shouldn't be making… Shouldn't be like… baking lots of hotel into Weaver.
**Josh Suereth (Google LLC)** 04:40 Yeah, I… like, I'm… I agree with Larn on there that Weaver is more generic than Otel.
But I also… and I understand that we weren't name… we weren't trying to be prescriptive with name spacing and stuff. However, in this case, I think It's clear. It's not about namespacing. It's not about like the dot of the namespace. It is exactly what does a template attribute mean?
And this is the line that I'm pointing at here.
That makes me think you should just use DOT.
Because, specifically, in Semcom syntax, the way we've defined it.
And we need to have a definition for templates across all Weaver, right?
And that… that doesn't necessarily have to be the OTEL way, but this doc says that it's a dot.
So whatever the first thing is, you put a dot and then key.
And that's how a template type is defined.
And I understand we could make it be flexible of like maybe you can pick your separator.
That's a decision we could come to, but I don't want to rush that as, like, an emergency bug fix. What I would say is, in your bug fix, I would switch to use DOT.
Always. That matches this. And then we could open a bug to have the discussion about should we allow more flexibility there or not, you know?
Oh, go ahead, Liudmila. Sorry, I wasn't looking at hands.
**Liudmila Molkova** 06:13 No, I just raised it.
The.
other point is… We cannot have different separators in different registries.
Because then all the breaks loose.
And either it's a registry property.
And then it's kind of… it stops making sense to me.
Or… It's always the same everywhere.
**Jeremy Blythe** 06:52 Okay.
So… I guess I'll just close that Pr, and I'll just make another one. That's really, that's really simple. That bakes in the full stop.
And fixes the actual boat ticket.
**Liudmila Molkova** 07:17 Cool, thanks for fixing it.
**Jeremy Blythe** 07:19 The There are… there's… As you found, there are some other places where we've already gone the other way, and I myself have gone the other way.
And already baked a dot in.
Like, I did it in the… the, the UI server thing, and it's baked into that, and that's how it builds the tree, because it separates by dot and understands namespaces. I get it, I've done it myself.
So.
But, previously… I had also gone the other way as well. So for MCP, specifically for MCP, I put in a thing which was the namespace separator, which defaulted to dot.
Because one of the MCP tools… is a browse by namespace tool.
Because Claude likes to go in and go, oh, It gave me all the HTTP things.
find its way down. Anyway… So I could roll that back as well, and just sort of throw it away and have… and then we'll be… It will be consistent, so I could do that in the same… I guess I could do that in the same PR.
**Josh Suereth (Google LLC)** 08:38 Do you know what I want to do for the MCP server, but I have no time?
is instead of the hard-coded string matching, that we take things and throw them into a vector DB that you can do hot searches on and things, and fire that at.
Right? Like… I don't know, there's a… I can find the article, I think it was from, Spotify, about optimizing Claude, and how to use less context, but it's not just, like, the fact that it searches for namespace makes it faster. It's if you can actually… if we can design a search that is somewhat semantic.
in nature.
But I can bulk read through a whole ton of crap, and give back a very small context for the thing you're looking for.
that is the ideal API. So, like, what Spotify has is this crazy-ass thing that researches their whole codebase and gives you back, like, you know, you can search through thousands and thousands of files and get back, like, the five things where the thing you're looking for shows up, but the thing you're looking for is not necessarily a raw string, it's like a semantic.
So, I feel like that's the direction we should move here, that would actually make it really, really awesome. But now it's no longer, like, namespace doesn't matter anymore. It's actually just, like, what's the… You know, the vector you're looking for in the… in the space.
So… I haven't had time to do anything meaningful with these insights, I just read. I'm like, oh, that's a cool thing to remember. And now I tell you, because someone else who's more useful will get them done, right?
Anyway.
**Jeremy Blythe** 10:12 Yeah, sometimes I'm asking… the agent, like.
I've got this new attribute. Where should I put it? And then the namespace is is useful.
Right now.
**Josh Suereth (Google LLC)** 10:23 Yeah.
Okay,
**Jeremy Blythe** 10:26 and.
**Josh Suereth (Google LLC)** 10:26 So back to… Am I sharing the notes again? Yeah.
I think we have a decision there of, like, I think we've decided on… I honestly don't think Weaver can function without having a decision around how to deal with template types, because the template types are too fundamental. So, like, with Ludmilla on using DOT, and your overall question, Jeremy, about where the line is, I think we still have to… Dance on that line.
I think what's happened over time is SemConf has started to look more like what Weaver's vision was, and Weaver has started to look more like Semconf. Like, it's been a two-way street, not a one-way street, like.
Semconf is now multi-registry by default.
Because we have so many multi-registry SEMCOMs spinning up. So, we no longer have, like, that… where that's a thing that only non-SEMCOM people care about. That's a thing everyone cares about. So, I think it's blending, but we'll have to figure out that line as we go. So, if you see anything else, call it out. We should probably try to address it quickly.
If we don't mind…
**Jeremy Blythe** 11:34 I.
**Josh Suereth (Google LLC)** 11:35 What?
**Jeremy Blythe** 11:36 I just… the last thing on that is.
I think that we've done things where we've, we've made, like.
Otel.rs that has Otel-specific things in it, because we wanted to sort of keep them separate… separate. I think they're, like, I don't know.
They're ginger helpers or something.
where we've like specifically called them hotel.
We're saying that Weaver and Otel is the same thing.
Actually.
Then, why not? Why don't we, like, go the whole way?
**Josh Suereth (Google LLC)** 12:11 I think they're blending, and some of those OTEL helpers, we actually can get rid of, or can make generic, because we've blended enough that it's… there's not really a difference anymore, you know?
So, yeah, I think that's actually… that's a good call-out. I need to go look at some of the OTEL things that we have, but, if I remember… It was things like extracting the right signal, right?
And… for doing a template in Jinja.
I think in a lot of cases, the new V2 layout makes that just simple.
You know? And, like, people using V2… it's no longer an OTEL thing, it's literally just a Weaver thing now, where in Weaver, we have a metric called out as a metric, we have attribute as a registry, right?
**Jeremy Blythe** 13:01 Yeah, and we also have, like I was saying, we also have policies.
that we've specifically built in Rica rather than baking them into weaver.
And if… If the direction is, like… But actually, everyone really wants to follow a tool.
Then… Surely those things should be baked in as well. You know, things like the… Following… following the namespace is even actually, it's a it's a policy.
That you have to add separately from just calling WeaverCheck, so then you have to bring these policies in.
Through the Weaver package, now, you can do that.
But what that's doing is telling you, oh yeah, you're using… you're using dots, and it's lowercase, and things like that, so shouldn't we bake those things in, and just make life easy?
If we're properly blending everything.
**Yordis Prieto** 13:55 Jeremy, I'm in that camp of like, I people, I, I come from this pro to this project to take advantage of people like you to be opinionated enough.
And I'm one of those that opt in to it right away.
Because, you know, like, from time to time, I join here and I see you guys, but, like, I don't have the time all the time to be up to date, right? So I would definitely appreciate tools telling me, hey, wink wink.
You're missing something.
**Jeremy Blythe** 14:27 Yeah.
**Josh Suereth (Google LLC)** 14:29 I… the only thing that gives me pause, Jeremy, is, Prometheus.
Like, I don't think Prometheus engages with template.
attributes at all.
And it could be that what we do is inside of Weaver, the data model, we use dots for everything Prometheus, and when they do Cogen, they convert the dots to underscores.
You know? But, like, Prometheus metrics today are kind of… are all underscore-based.
And so, there were… I don't remember what happened with it, but I remember Arthur was actually using Weaver in Prometheus itself.
Where it's not even OTEL.
And so… Again, like, I don't think that… Would engage with this.
Template type thing, and I think template types are a funny… Feature.
Right, but that would be the only thing I'd give pause, but I hear you, like, the… becoming more prescriptive, I think, is useful.
The line we've always tried to hold, though, is the out-of-the-box default can be prescriptive, but Weaver should be flexible.
So how do we get that balance right?
**Jeremy Blythe** 15:40 Yeah, I think it's something that we need to… We need to make… Clear, because it's unclear, but we need to make it clearer as we go towards V1.
**Josh Suereth (Google LLC)** 15:49 Yep. You know what would be useful? I can… I'll take another AI. We'll add this as a second decision.
Write down project principles.
This is… this is a thing I found, works really well, internally at work that I… I want to start doing more. We did this in the Open Telemetry specification. I don't know if you've seen this, let me… Let me find it quick.
There's also… this… there's also one for all of OpenTelemetry, but, where… is it actually in the spec? It isn't in the spec, it's not one of the other docs.
Umm.
Yeah. So, like, we have a set of principles here that are, like, you know, how we make decisions.
What our core values are, that sort of thing, right?
And this is really high level for all of OpenTelemetry, so I don't expect ours would be this generic, but we could have a thing like, you know, we have a principle of the default should be prescriptive, but users can escape into, you know, managing it themselves, would be like a principle of Weaver that we would write down.
And then that helps us all understand, like, how to make decisions, so we all make similar decisions as we make CLs, and if someone new to the project comes in, they can read it and be like, oh, okay, I buy this, you know, like, I'm in, kind of a thing.
What do you think?
**Jeremy Blythe** 17:09 Yeah, we do this kind of thing as well, but I think it makes sense, and it also, It helps the agents, right? So you started the, you've got the docs knowledge.
I actually added a thing in the, in the PR for.
**Josh Suereth (Google LLC)** 17:23 I saw that, thank you, yeah.
**Jeremy Blythe** 17:25 Coverage.
And we have some problems in coverage, by the way, but anyway, that's a separate thing. But this would be perfect to go into that knowledge area, right? Principles.
**Josh Suereth (Google LLC)** 17:36 Yep.
I'm actually thinking of actually putting it somewhere else, and then having the knowledge reference it.
Because I, I… principles, I think, like, are foundational and need to be kind of called out, so I might even have the README call them out.
Because if I remember right, knowledge is…
**Jeremy Blythe** 17:52 On the docs.
**Josh Suereth (Google LLC)** 17:54 It is under docs. Maybe it's okay there.
Yeah.
Just want to make sure that it's easy to find. Yeah, I forgot we made it.
We have the 4 humans and 4 machines, yeah.
Okay. Anyway, cool.
I think we have other topics, so, I do… I do want to check, I'll add this to the bottom, because we can delay, but, release this week.
Alright. Yordis, do you wanna talk us through some of your questions here?
**Yordis Prieto** 18:30 Okay, well, sorry for bringing my OCD to you, but I want to… Yeah, this is… again, I want to follow the same things. So, I… I replaced Weaver for, like, literally across all the programming languages. Like, I'm all in into the tool right now. So now, what is happening is I have, cross-organization things, so now I need to decide to put Weaver, outside the given repo.
Because it's always the same pattern for Go, Elixir, things like that. So… What should I name that repo?
I know it doesn't matter, but, like, you know, did that dash packages at the end in the Weaver package matter? Is that a language you use to refer to things? And, you know, that was just, like, okay, what should I do here? And if the answer is it doesn't really matter, okay, it's fine, but… I just wanted to, understand the lingos, and… Just give me, like, a package name for the intent of sharing templates and policies inside the template.
**Josh Suereth (Google LLC)** 19:45 Yeah, we… we can… so pack… the name doesn't matter, but that is how we're trying to refer to those. So, like, when you think about, like, a, a set of policies, the idea would be you package them into a GitHub repo, and then people can download the package and use it. And so, we call it packages because, like, yeah, I'll just show it.
The idea would be inside of this packages repo.
We also want to allow contribution, from other people, but there's, Inside of policies, there's two types of.
policies, you can have check and live check. We don't have any live check packages yet, but each one of these is an individual package.
And the idea would be, like, for naming conventions, we could actually have an owner's file for this. It has its own README, it might have its own set of people who own it and make contributions to it and drive it, but this should be a completely standalone package that is self-describing that someone can use independently of anything else.
for, like, your conventions. That's why, again, like, we have this weird syntax for how you get access to one of the packages inside of the packages repo. If the repo was just a single package, you wouldn't have to add this extra reference underneath it.
This is just what we decided for OTEL to get, like, a set of, you know, allow people to provide their own that they think are useful to everyone else. So, we're calling those a package. I don't know if we've kind of gone through any sort of real naming.
Decisions there, like Jeremy Ludmilla, do you remember if we did?
**Yordis Prieto** 21:29 No.
**Jeremy Blythe** 21:32 Okay.
**Yordis Prieto** 21:33 Okay, so then, packages… I'm gonna call it packages, then. Like, I know it doesn't matter, but, like, you know, the more I expose these tools, then people are familiar with it and know what to expect, so… What I'm gonna do, just put, like, the org name dash weaver dash packages, and exact same. Like I say, I'm… I don't try to add noise to… For people learning outside just what I'm doing.
**Josh Suereth (Google LLC)** 21:57 Awesome.
**Yordis Prieto** 21:58 Yeah.
And and the second one is somewhat.
Later to the same, like, learning from you, okay? Now I have… scatter around everything related to the, the actual, like, files defining the Weaver stuff.
Do you recommend, like.
centralizing a little bit the definition for sometimes packages, open source packages, like, I don't know, in Elixir, we have a few of them in the country.
But also, like, in the org, like, how do you normally prefer to manage that?
Especially that I was I don't know like in my head just thinking about, okay, centralization somewhat matters.
well, you will break anyway, observability in Datadog and stuff like that, like, it's not just about that, the blast radius, so maybe I thought it was important to sign off before, or, like, things like that, but, like, I don't know. I get analysis paralysis, and, like, here I am.
**Josh Suereth (Google LLC)** 23:06 Yeah, oh, am I… I'm not sharing the right tab, huh? Am I?
I was coming back to here. So, actually, I think… I don't know if you want to take this one, Ludmilla. So the.
or Jeremy. Jeremy, you've done it internally at a company. Ludmilla's been doing a lot of the work of, extracting it out for OpenTelemetry SemConf. Like, in OpenTelemetry SemConf, we are now trying to, like, split apart our semantic conventions across registries, so we could talk about what we do there and how we share Weaver files.
Jeremy, you do that internally, so maybe… Like, either Liudmila or Jeremy would probably.
I'll stop talking, because I think one of you might be able to walk through what you do.
**Jeremy Blythe** 23:50 I can tell you what we do at my company.
And… And it… So, what we do… is we have… We do have a central repo.
Where we've got all of the… Where, essentially, any application That's defining… It's Semantic Conventions, say, for a microservice.
It upstreams to this central.
repository.
And… and that's growing and growing. It's getting… it's getting big.
at some point, I think we'll do something like, Ludmila can explain in a minute, that happened with, like, with Gen AI, when that split up from the thing. But where we are, where we are at the moment on our journey, using it in the org, is we've got the one central repository.
That one, in its manifest, is dependent on the OpenTelemetry Semantic Convention Registry.
Because we're pulling into that.
And then each microservice, generally the way that it develops.
Is that the developer will be, sort of.
playing around, building the, some… pulling in some conventions from upstream, but maybe defining some as they go. So, like, the… so the developer has a nice, sort of, quick process, and then using Weaver to code gen.
And all of that, just locally in their service, and then they get to a point where they go, okay.
This is nice, but before I push it, I'm going to upstream all of the things that make sense to be upstreamed.
that are not 100% unique to this microservice only, and we have a rule that if it's absolutely unique to that microservice, its namespace is the name of that service.
So it will be, you know, my special service dot, and then things that are only related to that thing.
And people have to think very hard.
Could this ever be a thing that anybody else would want to use? And they have to like, okay, I'm going to hard name it as something that means it's unique here.
**Yordis Prieto** 26:07 So.
**Jeremy Blythe** 26:07 It's upstreamed.
**Yordis Prieto** 26:09 Real quick, only the non-service specific is what you put in the centralized, ripple?
**Jeremy Blythe** 26:17 That's… that's what we do, yeah, yeah.
If it's absolutely service-specific.
Like, you know, you've got an attribute that's about something that is totally unique to that service, that stays locally with that service, there's no point.
moving that upstream. So we don't do that.
Got it. But each microservice And this is fairly new. So it's only happened in a few places. But the intention is to do this across across everything we do. Each microservice also.
Publishers, The package of its… of the conventions that have been defined at that microservice.
**Yordis Prieto** 26:55 Right.
**Jeremy Blythe** 26:56 So when you go to our GitHub repo, you've got, you know, the release binary, or library, or whatever it may be, and then next to it, you've got the published artifact, which is the SemConf Which is related to that. So then, when you go to LiveTrick.
you can go. Oh, I want to pull in that because I'm live checking this microservice and just this microservice. And then you've got your nice constrained set of things that you're checking against.
Or you want, like our SRE team.
are investigating something, and they want to see, well, what's the sort of vocabulary for this microservice? I want to understand it. And they can go directly to that.
Thing, and look at the documentation that's published for it, and they don't have to kind of try and figure it out from the giant upstreamed central repo. So it's… we're just trying to find that balance between The 2, so that's the way we work.
**Yordis Prieto** 27:52 Yeah, that totally checks in, like, exactly, like, what I was somewhat expecting or thinking of, so that's really good. Thank you so much.
Do you use any specific tools outside Waiver to do those things? It's, like, most likely just GitHub Action or, like, a CI pipeline.
Pushing into the repo on Calais Day.
**Jeremy Blythe** 28:11 Yeah, it's just GitHub action. No other Tooling, just Weaver and GitHub and actions that we've built ourselves.
Yeah. Take care of all that, yeah.
**Yordis Prieto** 28:20 Yeah, that's cool. In that regards, like, sorry, to make a follow-up, like, about the service namespace, I get it as a top-level, like, naming spacing, but one thing I've been doing, and I think you guys mentioned this before, but I completely forgot, so I apologize, is that when When there is something that feels that belongs to another SecComp, what I've been… what we have been doing is just putting the service name, that exact same path, like. to make it made up thing, like HTTP, the status, made up thing. Is that normally how you would do it?
So we're trying to be, like, somewhat closer to the semantic convention, like, naming schema, because it's somewhat around HTTP, but it's not technically from SECM. So all we do is just to stick the namespace in the front, and then reuse dots in between to be closer, as much as we can to each other.
Because the other situation that we did this, and by the way, I do not like this from Semantic Convention, is that when the service is in between, and now there is a predefined list of things that nobody knows.
And we had to fight each other about it, and, like, we could never agree on it, and, like, there is a centralized thing that… oh, sorry, I forgot.
Which we… move away from. So that's why we put it out at the beginning, and then everybody else follow after that. So no more in the middle, you put your specialized thingy.
**Jeremy Blythe** 29:55 We only use the prefix of the service when it's absolutely unique to that service.
Everything else we try to make.
generic.
and then it goes upstream. And if if it's something like we.
We use AWS a lot, so… It Not all of that is in the… is in the hotel Semcoms library, like, things to do with AWS, right? Because there could be a billion things, right, that you want to describe.
But it's about an AWS service, so we actually… we're extending, like, by just putting it in the same namespace. So we have, like, AWS. and a whole bunch of stuff that doesn't exist in OTEL.
But that's fine.
**Yordis Prieto** 30:43 But do you own AWS?
Namespace, or you just decided to reuse the exact same?
**Jeremy Blythe** 30:50 So that it lands in the same place.
**Yordis Prieto** 30:53 Yeah, yeah, like, okay, this is where I need direction, because we tried that, and then we couldn't tell, okay, who is the funny what here? And, like, it becomes a mess. I don't have any strong opinion, but, like, from the Tooling perspective, right? Like, and, like, community, and understanding, and where to go to know, hey.
Yes, but there may be multiple people adding it to it. That's where, like.
The second part of trying to get help, because.
Like, I don't have any opinion, per se, like, a strong opinion, it's just like, okay.
Other than shared tooling and expectations, so that people don't make the wrong assumptions, and like, now, okay, well, yeah, that's not technically AWS, it's somebody else added there, and now we're talking about… to the wrong people.
Yeah. About the given key, yeah.
**Jeremy Blythe** 31:41 I see what you mean. You want to know. Was that defined internally by the by your company? Or is that? Yeah? So that's where the the provenance would come in. Right?
So, one of the things that… And I haven't run into that problem now, I'm just trying to help solve your problem, but, One of the things that we're… that you can make visible, but it's a bit… it's a little bit buried, I would say.
Is that you can tell, where… where you know where a convention is defined. You know where it's defined because of the provenance, and I can't remember. I think I've got it in a PR, but if you go to the… if you go into the UI to, like, the search, and you're searching around, I think I've got a PR, or I've got a branch somewhere.
That actually brings the provenance into the user interface, so as you're scrolling around and you're looking.
You'll see it there. And you can put that in the docs, and you could put it in the code gen as well, if you want to, like, put it everywhere.
**Yordis Prieto** 32:39 Oh, so is that like an actual Tooling? Sorry, I'm not too familiar with that.
provenance. If somebody can have a link, I can check it out later. But, like, it sounds like, at the end of the day, with that tool, just… it's, like, most like a racer of who owns what, so it's okay. It's just documentation and tooling of, like, look inside there.
**Jeremy Blythe** 32:58 Yeah, I mean, that's where it comes… you… you… you can tell from the schema URL Where everything is… was defined.
So every… I see. So every attribute name, every metric name, everything, you can… you can then see, oh, this one… this one was defined in this.
schema.
**Yordis Prieto** 33:23 I like it.
**Jeremy Blythe** 33:24 And then you can… so then you can actually tell, oh, you know… But again, again, you need to… We want to split it apart.
But we also want to know where the heck it came from.
**Yordis Prieto** 33:38 Yeah, and then in data, most likely you… in Datadog, it's like, at least that's what we use. If I do what I did, which is, like, you know, prefix everything, now it's like the two keys are far from each other.
So… but in the opposite realm, it's like, we don't have a tool in, like, the.
provenance, or, like, all these things to say, look, here's a way to think about it and go there, so now people don't know neither. And I'm sitting, you know, from the… platform engineering is like, okay, who's… who's doing what here? Like, I don't… I don't know what's happening.
Yeah, thank you so much, that's really helpful.
**Jeremy Blythe** 34:15 Okay.
**Liudmila Molkova** 34:17 I think the only critical choice you should make is to use SchemaV2.
And stamp schema URL on the telemetry you emit.
Because everything else you can do in multiple ways. One report of multiple repos.
put, I don't know, service namespace inside your attribute names this way or other way, as long as it's consistent.
And you can work either of the problems you face. Like, either way you go, there will be problems. If you have multiple repos, it's a pain. If you have single repo, the ownership becomes more complicated.
Either way, you have problems, and all of these problems are solvable if you use Schema V2 and stay consistent with whatever choice you make.
**Yordis Prieto** 35:12 I love it.
**Josh Suereth (Google LLC)** 35:16 The other thing I would say, keep coming here and asking questions, because when you run into problems, we can make sure… sometimes we'll have a solution, sometimes we won't.
But we'll make sure we will eventually, and we'll make sure it's documented, right? Because I think this is, like, what we need to just help everybody out, because everything you're asking is, super common questions that we hear repeatedly, and if it's not written down or, like, easily to find, we want to make sure that that gets fixed.
Is my internet bad?
**Jeremy Blythe** 36:00 I didn't think so.
**Yordis Prieto** 36:01 No, I can't hear fine.
**Jeremy Blythe** 36:02 Vincent?
**Josh Suereth (Google LLC)** 36:03 Oh, just the camera view of everyone is, I only get one camera shot every 5 seconds, so it's really, like, mind-bogglingly weird watching the Zoom call.
Sorry. All right.
Cool.
Chinsky Mural, yes.
All right, let's talk, we have 20 minutes left. Can we do a little bit on release planning?
Umm.
I will say, Jeremy, given what you found after the V1, V2 refactor, I really do want to rip the whole resolver apart and make it agnostic, so we're not converting V2 back to V1 to do resolution. Like, it's just… the number of bugs we've discovered in that is so high.
But thank you for fixing the most recent one.
**Jeremy Blythe** 36:51 You just looked at the third one.
**Josh Suereth (Google LLC)** 36:55 I don't know, did you… if you posted the third one between, like, 3 hours ago and now, I haven't looked at it.
**Jeremy Blythe** 37:01 Yeah, I just did it before the meeting.
**Josh Suereth (Google LLC)** 37:04 Okay, I haven't had a chance to look at it.
**Jeremy Blythe** 37:06 Okay, yeah, it's in. It just went green, so…
**Josh Suereth (Google LLC)** 37:10 Okay.
So let me go back to Weaver.
If we were to… look at… this… So what you're saying is, This one here is the last one.
**Jeremy Blythe** 37:27 That's the… yeah, that's the last one in the series of… things, they're all related to that V1, V2 conversion.
**Josh Suereth (Google LLC)** 37:35 Oh, should be left out of YouTube registry.
It is public when the group is imported from… Oh, crap, I missed that. Yeah, it was only supposed to do that for things that are private.
**Liudmila Molkova** 37:55 Wait, but it's still…
**Josh Suereth (Google LLC)** 37:57 It should have kept the visibility, though, shouldn't it? Yeah.
**Liudmila Molkova** 38:07 Isn't it the point? Why is it the problem?
**Jeremy Blythe** 38:12 The thing is, it's… It could go either way, but it's… if you resolve from a source file.
You get one behaviour.
If you resolve from a packaged file, you get this other behavior. The behavior needs to be consistent. the Prs, the 3 Prs are just making the package to do what the source does.
Now, it could be… What we're doing with a source file is also not what we want.
Yes, it's the point people.
**Liudmila Molkova** 38:45 Internal groups, internal.
**Josh Suereth (Google LLC)** 38:51 Yeah.
This might… this is probably just a bug with internal, or, like, the default, Publicity level of the thing.
Because this is the registry, right? The attribute group shows up.
But it's not… That's the catalog, the attribute group. This is not saying whether it's public or private. Is this a V1?
No, this is V2.
Oh, these are always public if they show up here, is that right?
**Liudmila Molkova** 39:22 Right, yeah.
**Josh Suereth (Google LLC)** 39:24 That might be the issue. It might be that when we load it, we aren't loading it as being public when it should be public.
**Jeremy Blythe** 39:33 So, My understanding… I should say, my and Claude's understanding.
Is that when you resolve from source, it makes it… It's… the public ones are pulled in as public.
When you resolve from a package.
The public ones are pulled in as none.
**Josh Suereth (Google LLC)** 39:55 Yeah, and this should be pulled in as public, yeah.
**Jeremy Blythe** 39:57 Yeah.
And that's what this fixes. It's like a… it's a… As usual, it's a load of lines for testing, and, like, one line for the actual fix, or a couple lines.
**Josh Suereth (Google LLC)** 40:15 Right, and this is… this was the bug, which we missed.
**Jeremy Blythe** 40:19 Yep.
**Josh Suereth (Google LLC)** 40:20 Yep.
Because it's in the frickin' conversion and the imports, and one group is not like the rest.
Oh, man, yeah. Again, this is another sign, I think, making V1-V2 split, like, inside of the resolver would make it easier to review code. This is subtle as hell. Thank you for fixing it.
**Jeremy Blythe** 40:49 Hey, thank you. Thank you.
I.
**Josh Suereth (Google LLC)** 40:54 It's the point where you're not spending thousands of Claude tokens to fix little bugs. Like, we gotta… we gotta clean this up.
**Jeremy Blythe** 41:00 God.
**Liudmila Molkova** 41:01 Yeah, move to Gemini.
**Josh Suereth (Google LLC)** 41:04 Then the thousands of tokens are cheap.
Okay. Alright,
**Yordis Prieto** 41:14 I was really excited, Josh, for… sorry.
**Josh Suereth (Google LLC)** 41:17 Yeah, no, go ahead.
**Yordis Prieto** 41:19 No, I was really excited that I was in Rust, because as I'm working on a tool that it does something like Rego, but without Rego in any unstructured data for linting.
The only tricky bit is that I went all in with WebAssembly, so I can run untrusted plugins and stuff like that. I don't know if you guys talk about it or are interested, but I'm all into WebAssembly, so I can inject, like, plugins, generators. In that tool, I also have, like.
template generation. It's not, like, Weaver, but it could be for any unstructured, like, YAML, whatever.
**Josh Suereth (Google LLC)** 41:54 That's cool. Yeah. Yeah. Yeah. We, I've been doing a little bit with WebAssembly, but just enough to know boundaries and design. And I know for a fact that the way we do threading.
We would face some struggles moving to WebAssembly initially, unless we start building the right abstractions. Yeah.
**Yordis Prieto** 42:13 Yeah, yeah, that is also a concern, although now they have threats in WASI P3, if I'm not mistaken.
**Josh Suereth (Google LLC)** 42:21 Right, it's more, our libraries don't have WASM support.
The ones that we're using. The library we use for threading, once it has a WASM boundary, then we're fine, right? Yeah.
**Yordis Prieto** 42:30 I see Nice.
**Josh Suereth (Google LLC)** 42:32 Cool. Alright, so this, this looks good, I think… There's a few RenovateBot things to look through. I want to go through the project quick.
And check on any tasks we wanted for release before we finish release planning.
All right.
I don't think anyone's worked on this.
This is the one we talked about earlier, Jeremy, is that right?
**Jeremy Blythe** 43:05 No, that's a different one, but
**Josh Suereth (Google LLC)** 43:07 It's a different one. Okay.
**Jeremy Blythe** 43:09 Yeah, that's… that's a different thing. We don't need to do that this time. I have a plan to get to that.
**Josh Suereth (Google LLC)** 43:15 Okay.
**Jeremy Blythe** 43:18 We have to do that, yeah.
Yeah, the one we discussed earlier was 1775.
which was the namespace thing, that what I'll do is I'll… I'll probably just delete that PR and do a new PR that's… Just for the doc.
to actually fix that book, because we should fix that bug for the release right? Because it's it's not good.
**Josh Suereth (Google LLC)** 43:45 Yeah, like, I think we should get the bugs into here. What did you say it was again?
**Jeremy Blythe** 43:50 The PR is 1775, I think.
**Josh Suereth (Google LLC)** 43:56 Why are you not finding it? Do I have to just type in 1775?
**Jeremy Blythe** 44:03 We're looking for issues.
**Josh Suereth (Google LLC)** 44:06 It looks for pull requests, too.
**Jeremy Blythe** 44:09 Oh.
**Josh Suereth (Google LLC)** 44:11 There it is, right here, right?
**Jeremy Blythe** 44:13 Yeah, that one.
**Josh Suereth (Google LLC)** 44:20 You'd think with all the GitHub I do, I'd be better at this. Anyway, this one, I don't think I'm gonna get to for this release, sadly.
But I can, I can review your PR. I think it's actually more urgent that we get the, live check fix out for the stop report stuff.
Yep. So, once this is through, I think we try to cut a release to get LiveCheck working. So we get that through, we make sure the downstream check passes, and then we can cut a release?
**Jeremy Blythe** 44:50 Yep.
**Josh Suereth (Google LLC)** 44:51 Cool.
Okay.
**Jeremy Blythe** 44:54 Today, I should… I should be able to do that today.
**Josh Suereth (Google LLC)** 44:57 Okay.
The next thing I want to work on, which I… we still need to be moving towards… why are you doing this?
I used two fingers, but I wanted to scroll this way. Here we go.
The next thing I think we I want to go through here and kind of figure out what is, like a 1.0 Weaver release blocking for the next release.
and what is not, and pull things into, like, needs design that we're going to consider 1.0 release blocking. Same for ease of use.
But the thing I really want to do is go rewrite the resolver again.
So, I might nerd snipe myself and do that anyway, because I think that might lead to less bugs in the long run.
But… I don't know, how do you guys feel? Like, do you think it's worth taking a crack at that, or should we just keep churning down bugs quick?
With what we have, cut a 1.0, and then we can redo the resolver afterwards.
**Liudmila Molkova** 45:59 I think for me, the main blocker for the Vivan is we never actually published anything.
In V1.
And, we… kind of want to move semantic conventions to V2, the number of versions we have. Anyway, so… If we have… I feel like once we start, doing publishing.
in Semantic Conventions.
We'll discover a whole set of new subdelicious.
**Josh Suereth (Google LLC)** 46:36 Yep.
**Liudmila Molkova** 46:37 Maybe a low priority, because, like, I don't think we are able to validate The published thing, reliably, until we… Start consuming it somewhere.
It's like, I would… I would be happy calling it V1, but not stable yet, RC, after we publish semantic conventions.
And after we successfully consume it from another federated repo like Semplank GenAI.
**Josh Suereth (Google LLC)** 47:07 Can we start publishing… can we start publishing before we hit V1 with Weaver? And then… Like, because we're still making point…
**Liudmila Molkova** 47:15 releases.
**Josh Suereth (Google LLC)** 47:16 I'm just saying yeah. Like, I'm trying to figure out what we need to do for v one, and I agree with you. Publishing needs to stabilize. What's the blocker from publishing in Semcom right now, the new thing? Like, is there work that we should be so I don't waste time redoing the resolver because I want to, and I spend time on things we need to get done.
Is there… is there work I should take on there?
**Liudmila Molkova** 47:40 Yeah, so, I'm back, and I was planning to return back to some of the issues, so… Pasting in the chat the tracking issue for.
This one.
**Josh Suereth (Google LLC)** 47:59 Oh.
**Liudmila Molkova** 47:59 I.
**Josh Suereth (Google LLC)** 48:00 Okay.
**Liudmila Molkova** 48:00 Think.
What?
Is.
So there is one more thing that's… does not… so, okay, imagine we do minus minus V2 in SemConf. What's going to happen is a bunch of, crap, like… Mmm.
The spans that should be refinements will show up.
We'll need to clean them up.
So, first, we need to… update… the existing Semantic Conventions.
And there are maybe a handful of them, I should list them here, that produce this crap. I think database is the one.
And RPC is the second.
We switched, I think, everything else.
And then, what we produce will start to make sense.
We can publish before, it's just we should somehow communicate that it's broken us.
**Josh Suereth (Google LLC)** 49:16 Yeah, I… I get… I get what you're saying. We could… we could start publishing, but it won't be consumable until we fix other things. But we could actually get this… we could get this started. So what… what… what I'm thinking is this here.
Generate schema next.
Can we cut that to 1.0 sooner rather than later?
**Liudmila Molkova** 49:39 Yeah.
So, let's, There are two open items from before, right? So, even before we can do minus minus V2, we need to resolve, like, this, in this long list of things.
That migrates the OS and the entities without identifying attributes.
I'll… Yeah.
**Josh Suereth (Google LLC)** 50:07 I can do a crack at entities because I feel like.
**Liudmila Molkova** 50:09 good.
**Josh Suereth (Google LLC)** 50:10 My purview there, a little bit, as well.
I'll do a crack on everything but Zoss.
**Liudmila Molkova** 50:17 I will…
**Josh Suereth (Google LLC)** 50:18 us.
**Liudmila Molkova** 50:18 Yeah, yeah, I think it's doable now. I'll ping mainframe people to see, maybe I can help them if they don't have capacity to work on this right now.
**Josh Suereth (Google LLC)** 50:29 Okay.
**Liudmila Molkova** 50:30 And then…
**Josh Suereth (Google LLC)** 50:30 Or,
**Liudmila Molkova** 50:31 Yeah.
**Josh Suereth (Google LLC)** 50:32 For entities that are still experimental, I might… like, I'll pick some identifying attributes, but I'm gonna call out and caveat for every maintainer to understand.
The identifying attributes are not permanent, we can change them while they're experimental so that we don't run into as much friction? Okay.
Alright, that sounds good.
By the way, for context, all the entity spec work landed, so we can actually start landing SDK implementation soon.
Nice! And do code gen, possibly, after that, so… That's pretty exciting.
That's only 3 years in the making, when it probably should have been 1, but we're there.
laughs Okay, cool. Yeah, okay, so this sounds good. So I'll… instead of redoing the resolver, we'll start working on this and then pound on bugs. I think if we run into another situation where Jeremy's Claude finds 4 bugs in Resolution Engine.
again, then I'm just gonna take a crack at refactoring it so that we can more easily read the code.
and fix problems, because again, going from V2 back to V1, back to V2, It's so convoluted.
You know, it was… And the more we press on it, the more, like, complex crap goes back into it to fix real subtle issues.
Yeah.
**Liudmila Molkova** 51:56 Yeah, we can do what we can do. We don't need to publish it yet, but we can prepare everything to make it happen.
And by doing this, we will also maybe find all this additional resolution bugs.
**Josh Suereth (Google LLC)** 52:10 Yeah. Okay, so, like, we could set up the Weaver package flow, just not publish the result of it.
**Liudmila Molkova** 52:17 Yeah, we can't even check it in in the repo.
**Josh Suereth (Google LLC)** 52:21 Yeah.
**Liudmila Molkova** 52:21 I don't know. It's very hard to discover.
**Josh Suereth (Google LLC)** 52:25 Your OTEP was approved, right? So we can start, like, at… when we're ready, we can start actually pushing to OpenTelemetry I.O, or do we need other approvals?
**Liudmila Molkova** 52:34 We can start pushing to OpenTelemetry IO. I wish we had the spec changes to document the new format because we we did the OTAP is merged, but the spec changes are pending.
**Josh Suereth (Google LLC)** 52:46 Okay, that's also something I'm happy to take on, too, if you want.
I don't mind beating my head against the wall for spec. Like that's that's been my life, you know. Like you throw a PR, you wait 12 years, it's approved, you get it through, that's fine, whatever.
**Liudmila Molkova** 53:04 Yeah, it will… if you can take it, it will be awesome.
**Josh Suereth (Google LLC)** 53:07 Okay, unless you already have one.
**Liudmila Molkova** 53:09 No, I don't.
**Josh Suereth (Google LLC)** 53:12 Okay, alright. Do you think that has to describe the… Well, actually, I'll make the PR. I'm going to… Just tentatively run this by you, since we only have 2 minutes.
The spec, I think, should delegate the actual contents of the file to… Weaver.
So, in the specification, we'll say, hey, we have a file, here's its format, but I'm gonna say the format is the Weaver published format that is documented here, here's the schema. It will be owned and updated by the Weaver project, and here's restrictions on its… Compatibility, right? About how it can't make breaking changes, that kind of stuff.
**Liudmila Molkova** 53:53 Yeah, I think only the.
**Josh Suereth (Google LLC)** 53:54 We'll see how that flies.
**Liudmila Molkova** 53:57 Yeah.
**Josh Suereth (Google LLC)** 53:59 Exactly. Yep.
Okay, cool. And then you said there's another question in chat, so let's go back to… The meeting notes.
**Yordis Prieto** 54:07 Sorry, okay. Weaver and logs. Do I supposed to put logs there as well?
**Liudmila Molkova** 54:16 events.
**Yordis Prieto** 54:16 Genlog.
**Liudmila Molkova** 54:17 Answer there.
You cannot codegen logs, because there is no definition for the log per… per definition of the log, it's anything. But there are events, and you can, document the event, you give it a special name.
And you can then call Jen the event.
**Yordis Prieto** 54:35 Can you be more opinionated?
**Liudmila Molkova** 54:38 Like, explain what, how.
**Yordis Prieto** 54:41 like, that special naming and annotation that you're hinting to be like, this is a log, event log, whatever that means. I was about… I thought it was the event, but I was not sure about it.
**Liudmila Molkova** 54:56 So the event, like when you do the events in the schema v2 or group type event, this is.
**Yordis Prieto** 55:03 Yeah.
**Liudmila Molkova** 55:03 But you are defining a log with the name, which is event.
**Yordis Prieto** 55:09 I get it.
But most people will be like, where are my three things that I want to document?
Because, like, what is event for? Is for law… event log? That's… that's where you came?
**Josh Suereth (Google LLC)** 55:22 Yeah.
Yeah, in OTLP, we call it the logging signal, but we consider what it sends to be events.
So, like, we… in OTEL, an event and a log are the same thing.
The login signal and event signal are the same thing, but in Weaver, we call them events. If you're sending raw strings, like, if you want to send strings, and you want to make sure there's a set of attributes attached to it, that would be an attribute group.
That you would define. And then you could say, like, does this log have this attribute group?
But that's, like, a really not-specific thing. So our opinion is, you should be defining events, they should be structured, they should have all kinds of data in them, it's easily… easy to parse. So in terms of our opinionation here, we… like, it's basically, don't use logs, go Observability 2.0, everything's an event.
And.
**Yordis Prieto** 56:14 Yeah, well, but everything, every single… Yeah, but then the tools in between, like, not that I disagree with you, but, like, how do I replace S-Log in Golan and, like, Elixir Logger and…
**Josh Suereth (Google LLC)** 56:27 No, SLOG is an example of, like, you… so we consider something coming out of SLOG an event. SLOG, you have a string, and you have a set of attributes, right?
**Yordis Prieto** 56:34 Right, right.
**Josh Suereth (Google LLC)** 56:35 You can, you could represent that as an event.
**Yordis Prieto** 56:40 Got it.
Okay, yeah, the transformation is whatever meaning you want to give it. Okay, cool.
**Josh Suereth (Google LLC)** 56:46 Yeah, but I hear what you're saying. Liudmila is probably better to answer this. I'm just… Trying to help with my own view of the world there, right? Yeah.
**Liudmila Molkova** 56:57 Try it out, and let us know what doesn't work, because it should work.
**Yordis Prieto** 57:03 Okay, yeah, I'm gonna use the event as the semantic as the same as log anyway. Okay, cool, great, thank you.
**Josh Suereth (Google LLC)** 57:10 Yep.
Cool.
All right. Thanks, everybody. See you next week. See you.
**Yordis Prieto** 57:16 Bye.
