SIG: JavaScript SIG
Date: 2026-08-26
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Trent Mick 00:00:39 Hey, Marc. Haven't seen you in a while.
Audio.
You're muted.
Marc Pichler (Dynatrace) 00:00:47 Hey.
Trent Mick 00:00:48 Inc.
Did you do the biking trip then, finally?
Marc Pichler (Dynatrace) 00:00:53 Yes, it was… it was very fun. I can definitely recommend. It's supposed to be one of the best ones in… in Europe.
Trent Mick 00:01:03 What was it?
I didn't know where you were.
Marc Pichler (Dynatrace) 00:01:05 was, from Salzburg in Austria to, Grado in Italy.
Trent Mick 00:01:11 Okay.
Marc Pichler (Dynatrace) 00:01:13 Yeah, so it's around 420 kilometers.
Trent Mick 00:01:18 Over how many days?
Marc Pichler (Dynatrace) 00:01:20 We took… way long. That's fine. I think we took, like, a week.
To do it, but we, took some break days in between. There was rain one day, so, we opted to, Take a spa day instead, which was fun.
Yep. That's cool. Okay.
It's, all over the, ski resort towns there, and in summer it's, it's nice, because you have all the amenities of, like, a skiing resort, but… Nobody's skiing there, so,
Trent Mick 00:02:05 So they're pretty empty? Is that why you can just, like…
Marc Pichler (Dynatrace) 00:02:07 Yeah, it's somewhat empty? Yeah, it was mostly hotels, yeah.
Trent Mick 00:02:12 Okay, and because it's empty off-season for skiing, you can just decide on the day of if you're going into a particular.
Marc Pichler (Dynatrace) 00:02:19 Yeah, exactly, so that's…
Trent Mick 00:02:20 That's great.
Marc Pichler (Dynatrace) 00:02:21 Yeah, it worked, yeah.
Trent Mick 00:02:23 Yep, yep.
Marc Pichler (Dynatrace) 00:02:24 So, yeah, it was fun.
Trent Mick 00:02:26 Nice, nice. What kind of elevation game were you dealing with?
Marc Pichler (Dynatrace) 00:02:30 Not much I think of, or… I'd have to look it up on the Garmin thing, but,
Trent Mick 00:02:36 Not… not crazy.
Marc Pichler (Dynatrace) 00:02:37 It was more through Austria, and then, once you're in Italy, it's basically just downhill, which is very fun.
Nice thought. Yeah.
Alright.
Let's get started with the meeting, then. Hello, everyone.
I agree.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:03:03 Hello.
Trent Mick 00:03:05 We have a 100% Attendees as maintainers today.
Marc Pichler (Dynatrace) 00:03:11 Nice.
Trent Mick 00:03:14 So far.
Marc Pichler (Dynatrace) 00:03:22 Alright… Looks like it's just… just maintain us today. I wanted to do, like, a big announcement for, welcoming Marylia to maintain us, but everybody here knows already, so… No, you had to maintain Marylia.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:03:47 Yes.
Marc Pichler (Dynatrace) 00:03:48 Pretend you're a subscriber.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:03:50 rice.
Trent Mick 00:03:53 Shouldn't be surprised.
Marc Pichler (Dynatrace) 00:03:58 Welcome to the maintenance group, Marylia.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:04:00 Thank you.
Marc Pichler (Dynatrace) 00:04:01 They were, move you to the group later. This is queued right now. So, once it's… Marched, I will send the invite, and… yeah, welcome.
Trent Mick 00:04:16 Did you just queue that? There's a… Yeah, yeah, welcome. Sorry, I got onto Mechanics already. GitHub has an incident right now, so things aren't being scheduled, so anyway. Sorry.
Daniel Dyla (Dynatrace LLC) 00:04:31 If maintainer promotion depends on GitHub, I'm not sure anybody will ever become a maintainer again.
Trent Mick 00:04:37 Yeah, it's all frozen now. No more releases.
Marc Pichler (Dynatrace) 00:04:47 Alright, yes, I guess, let's jump right into the first topic of the day, then,
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:04:57 Yeah, so that one was the one that I brought last week, without Trent here, just so I can plead my case without Trent saying, like, no, it's all wrong, but now Trent is here, so… Yeah, I saw that you replied here, but yeah, I wanted to just bring the topic for other people to give their opinion as well.
Trent Mick 00:05:18 Yeah, I don't have a prepared, like… Digestible summary for this meeting, really, and so, unfortunately, it requires people to Engage a little bit.
With the issue.
Yeah, I don't know… I don't know how strongly we're both gonna disagree on this one. So, like, I'm proposing a significant change as part of… Working on the code path for start notice decay, which is… I think we're all agree is intended our replacement for the new Node SDK path. It'll be a code path that supports Roughly, with some small breaking changes, the environment-based setup of an SDK And declarative Config, which is the… would be the major new feature part of that. So, this… PR… finishes and completes the env-based thing? Sorry, the en-based.
configuration of, because mostly the focus on start node SDK code path had been about dealing with declarative config.
That's… declarative config, I think, is mostly done. There are issues open for remaining to-dos for covering all of the different, Parts of the declarative config schema. Some of them are just we need to wire it up, and some of them are we need to… add support or refactor support for different things in our SDK components to support features that are requested by declarative config.
But this is the other half of that. So this is the… supporting the… already… Well-known and defined, environment variables defined by the spec before declarative config existed, and getting start node SDK to support that… that code path. Some of that existed already, And so this… PR is kind of two things. It's… one is… Finishing and working through the edge cases of supporting, and based setup of the SDK.
And then the other thing is the… It does a major architectural decision change on how that's done. So what, the design of the configuration package before had been is that you ask it to create a configuration model, which is our, kind of.
in-memory JavaScript, TypeScript model of a declarative configuration file, which has generated schema.
In the configuration package, but it would also create you a configuration model based not just on… Declarative config file, which… which was the main reason it was created to start, but also, based on environment variables. So, the design idea there had been that, the… complexity of… Creating a config object.
From either a declarative config file or from environment variables was in the configuration package, and then you get back this configuration model thing.
And then the next step is, to create all the SDK components from that configuration model.
And so the idea… design idea before was configuration package would give you a configuration model, whether or not the user was or the system is using environment variables, declarative con… or a config file, and then the SDK, package. Right now, the SDK node is the only one that this is relevant for, would use that configuration model and build all the all the SK components. The change in this what I've proposed in this change as part of finishing the environment path, was to change the configuration package to only deal with configuration files. It just does the declarative config schema model, and if you have a YAML file, it'll give you back a configuration model. Otherwise, the SDK, if, configuration file is not being used if it's still just environment variable path, it handles parsing the environment variables itself.
And the comment that's up here was kind of my defense for why I wanted to go that route. It is a significant architectural change, I'll give you that.
And maybe a departure from what some of the original design intentions were for the configuration package, so that's why it's a little bit controversial.
And would welcome review from others.
So that was a, like, crazy long thing as just an introduction for a thing that's even longer, so I apologize.
For lengths.
Marc Pichler (Dynatrace) 00:10:19 So… I did look into this a little bit, before the call.
And… I have one or two questions, so the first one is, the move… of, like, the moving… moving stuff from the configuration package to, the node SDK package.
I suppose what… Prompted this was mostly the… resource detector, MVAR, right? That's what you were starting with.
Trent Mick 00:11:02 That gave them the… the clearest example of what… why I thought… It was a bit of a leaky abstraction, having a configuration model trying to cover nv config.
So that was… Yeah, one of the points, probably the easiest one to argue, yeah.
I tried to lay out some of the other… some of the other points in here, and I don't wanna, like… biased too much by taking all of the airwaves here, but, the error handling was clearer, I felt, if… the SDK create step was directly handing me… handling the environment variables.
there was some code sharing, the code actually ends up being a little bit smaller, because obviously Node… the current path, the new Node SDK last thing was already doing environment variable parsing, so… Some of that code was reused.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:12:11 yeah, to give context of why I created that the way it is today was mostly because I wanted to have a single plate that had to deal with configuration, so… Now it doesn't matter which one you create, you know that it's gonna be on that package. The way that it is right now is like, oh, I need to update the SDK node package and the configuration package. If there is something that we want to change that is supported by both environments and the, like, the file, you have two packages to change now.
Compared to just one. So that was one of the reasons, like, everything's kind of, like, confined in a single place. Your… whoever's using the model is the same And because… For the… the function, like, the start itself.
I don't think the start should care if it is coming from an environment variable or a file. It's just, like, what is the config that I should be using? So this is why I like to abstract to just, like, the model. You have this package that deals with the model, so you might have things that are… setup or not, depending if it exists only on the file or only on the environment variable. You can have maybe, like, for example, for the resource detector that we only exist on environment variables. You can create just for that case, and not add for the file, and you still have the check when you use… so that is what's kind of, like, the idea behind everything contained in a single place.
So, yeah, just wanna… because even if it is now saying, like, okay, now the environment variable, like, the resources.
Like, the object is just one if it is from the file now, because it only… parse what exists on the file, so you don't have to think about the environment for about the way that, like, Trent did here, right? So it's just like, you have this config model that basically parse, creates an object, but then when I'm using if I'm using environment variable, I still need to change this somehow, if I'm adding the resource on top of that. So that is why I thought it would be… could be confusing, so I guess that is where the… the difference is here, that I was like.
I'm not sure if I agree with the going back to Like, making that distinction on who is using, not on the package of the configuration itself.
Trent Mick 00:14:36 Oh, the… the… So, like, I understand the desire of being able to encapsulate all of the configuration, the configuration package.
That the hotel noters or detectors equal all was… Kind of a straw that broke it for me in that… The declarative config spec is, of course, not going to… Ever promised to cover… Sorry, let me say that again. The declarative config spec came after, and as a response to the… the specified SDK environment variables not being expressive enough. So, I think we can always rely on the declarative config schema is always going to be a superset of the environment variables that are defined in that section of the spec. That excludes, though, any of the hotel underscore node specific things. We don't have a lot of them, some of the other languages have more But it's never gonna fully cover… all… environment variable configuration that you might have. I think probably… It… it's limited, so this… this kind of… not being able to cover everything for us is probably limited, because I don't think we're going to be adding many or any hotel underscore new environment variables. If, I get the sense that the direction of OTEL is we prefer declarative config, and that's where any kind of new, richer config stuff will come from, so… There's some… a limit to the leak there, at least.
That said, I don't… I don't think the… the design that config is only ever going to be decided in the configuration package is… purely going, like, can stay, because we already have this… this leak of this one case. And so you do need… A little bit of awareness of… Where the configuration's coming from outside of the configuration package. I mean, the… even to handle the semantics of node resource detectors all is one case, but the, like.
for good error messages, you also need to leak out that stuff. That can just be a string that gets printed things, so, like, you can deal with it either way. Both designs will work.
So… It's a bit of a preference call.
Like, I don't think either direction is gonna screw us.
So…
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:17:20 Yeah, for, like, for reference, like, a lot of the other languages are doing the same way that it is being done here, so we know that it works. A few of them do it.
the way that it exists right now, and that also works. So there is not, like, a clear, like, guideline on how this should be done. There's, like, no convention on how this should be handled, so there's no really, like, wrong… yeah, it's kind of like… a preference, and what I created that way was mostly because I went to the ones that did this way and asked for their feedback.
and say, like, did you like, at the end, what you created? Like, for, like, Java and Go that was doing this way? Because I say, like, I'm thinking of doing this other way, and they say, like, oh, I should have done the way that you did it. So that is what was my signal to do the way that I did. But again, it's… We will work both ways, it's just a matter of, like, whenever we need to, like, maintain, you have to pay attention to different things, I guess.
Marc Pichler (Dynatrace) 00:18:30 One of the… things I was also going to ask is, there's currently no way to express language-specific… Options in the config schema, right?
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:18:46 So there is a session for language-specific, we just didn't add anything for JavaScript, so that was actually the other thing that I was gonna bring up. Nothing is stopping us to just go to the declarity config and say, like, hey, we want to add those extra stuff, and just be part of the file as well.
And match whatever is missing, like, there is no, like, stopping us from doing that.
Trent Mick 00:19:18 It's a little bit hard to know without… concrete examples there, I guess. Like… We're not gonna get something added to the main part of the… Schema that is, like.
I don't know. I don't have a concrete example, so I don't know if we really hit that case other than this. Yeah.
David Luna Bistuer 00:19:43 One question, having both in the… so having all in the configuration package.
if I'm… if I understand correctly, it assumes that everything could be modeled.
With a single… with a single model.
Even though it comes from the file, it comes from environment… Okay, I guess The declarative config came from because the environment was not… enough, or not expressive enough, so I think it started from there.
So now it's… It's… it has parity with the environment, so the creative environment has parity, but I wonder if that is going to last.
So, if maybe, I don't know, it's going to be deviating, so other… So, are we certain that maybe conflicts from environment and from the clarity communication are going to converge all the time, or are we going to… go different routes. And maybe there is some situations that we cannot express The same model, the same declarative configuration with With environment variables, or the other way around.
Marc Pichler (Dynatrace) 00:20:50 I think the other way around should not happen, since there's a freeze on environment variables being added.
I'm sorry, Marylia, you also wanted to say something. Yeah, I was gonna, yeah, I was gonna say exactly.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:21:00 Medea, yeah.
Trent Mick 00:21:02 So I don't… yeah, okay, I'm not sure where the normative language for that is. If there is a freeze, what I did find is a conversation on… what was an open issue, but it was closed by a stale bot, between Jack Berg and Pellard, who I don't know his actual name, he… he's… a big, strong maintainer to go.
Daniel Dyla (Dynatrace LLC) 00:21:27 Robert.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:21:28 Robert.
Trent Mick 00:21:28 Robert, okay, yeah. About them kind of agreeing what… on… what the intent would be, and so they were, like, musing on the idea of, yeah, freezing environment barrels. So I think the one example is hotel metrics.
exporters, for example, that the environment variable would not support new names that declarative config might add, kind of thing.
Daniel Dyla (Dynatrace LLC) 00:21:55 I'm not sure.
Trent Mick 00:21:55 Arguably, that also…
Daniel Dyla (Dynatrace LLC) 00:21:56 don't eat…
Trent Mick 00:21:58 No, I don't… that's what I don't think. It's official, but, like.
I use that as kind of a minor point for arguing having the separation as well, and that the configuration package Yeah, in that the two things might… Arguably could be more difficult with the configuration package trying to create a config model over both environment and… File, but if… environment is meant to freeze, but file is not, and that it gets harder to… To score that.
David Luna Bistuer 00:22:28 So if environment is meant to freeze, it means that the logic that we have for our environment shouldn't change.
In time, but the one in the declarative config is going to change.
So, talking about, changing code for both sides, it's… if the AM is freeze, is frozen, that code path is not going to change.
But the other one, it's going to change as it evolves, right?
Trent Mick 00:23:03 That's my understanding.
David Luna Bistuer 00:23:05 Okay.
And then, I don't know, I wonder if that's, Probably, if that DM is going to be frozen, it means that… I don't know, then… Not in the near future, but in the future.
Declarative is going to be the way to go, and some… MV is going to be deprecated.
Trent Mick 00:23:31 Well… and will never be removed, I think is also the…
David Luna Bistuer 00:23:36 games.
Trent Mick 00:23:36 for another comment from Jack Bergen, that, like, you know.
U.
They'll say in Node.js, we do major versions willy-nilly, but, you know, we've got other… got other concerns, like the Java agent will… probably always support ENV, and I wonder if we might always support ENV configuration as well. So, I don't know, that's a long road.
To get there, but… like, from an internal design, and as I said, I think either of these designs, another one's gonna screw us, but, As an internal design, it felt.
Safer for me to…
David Luna Bistuer 00:24:11 Yeah.
Trent Mick 00:24:12 Have less code to… by separating those, but… Anyway.
Marc Pichler (Dynatrace) 00:24:22 I guess we need to, look into it a bit further and, keep discussing on the PR.
David Luna Bistuer 00:24:35 Alright.
Marc Pichler (Dynatrace) 00:24:36 Unfortunately, I'm not sure I… half, I'm leaning one way or the other yet. I can kind of see both ways working out.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:25:04 Yeah, we also spend a lot of time on this discussion. I see there are, like, other topics from other people. So yeah, take a look. Yeah.
get your opinion, and I'm away next week.
So… I won't be able to comment on that. I'm going to… to visit you, Mark.
the whole Grafana is going to Vienna.
Marc Pichler (Dynatrace) 00:25:26 Oh, nice.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:25:27 You're gonna see the entire company just… all over Vienna.
Marc Pichler (Dynatrace) 00:25:32 I will look out for the logo.
Marylia Gutierrez (Raintank, Inc. – Grafana Labs) 00:25:34 Oh, you're gonna be… they're gonna be, like, all the event people will be wearing orange, so you're just gonna see orange all over the city, but yeah.
Marc Pichler (Dynatrace) 00:25:42 Yes.
Alright, so let's continue discussion on the PR here. And… Let's move on to the next one.
This is Jackson's topic about, inference migration skill.
Oh, I think the microphone is not working.
Alright, so I guess this is a card for reviews, I'm… I have had a look at this. This is the, so, Open Inference had this, donation… Proposal, and that was accepted.
If I recall correctly, And I think that's what's kind of been donated, and the plan is to move stuff into the JSContrib rep repo.
This is a skill to, kind of aid in that migration.
So… I wrote… Take some time to review this one.
Thanks for bringing that up here.
And, I guess that would then also… opened the, possibility of adding other skills as well, because it's the first one that we would add to the repo. I had also one that I had planned to add, but didn't get around to yet, so… Might be a good opportunity to look into that as well.
Trent Mick 00:27:35 I'm far from the person to review the specifics of a skill, but if we get to a point where we've migrated basically all of the open inference instrumentations, is this… we'd remove that skill then? Like… It serves the purpose of specifically getting through that list of things, yeah.
Okay.
We're going by… facial expressions here, so, yeah, okay.
Marc Pichler (Dynatrace) 00:27:58 Those are sort of my understanding of how it would work here. So… Once it's done, we can remove it.
haven't looked into the details, but I think the… at least the description of what the skill does gets, loaded into context every time, so, Save some tokens by removing it later.
Trent Mick 00:28:23 is… Yeah.
Is a 700-line skill big?
blank.
Marc Pichler (Dynatrace) 00:28:33 I've seen… I've seen…
Trent Mick 00:28:36 And whatever, if that's what it requires to cover the topic, then that's what it requires.
Marc Pichler (Dynatrace) 00:28:40 I've seen them in all kind of sizes. I've seen very small ones, and I've seen, ones that were, that triggered warnings in Cloud Code, so,
Daniel Dyla (Dynatrace LLC) 00:28:55 Seems almost a philosophical question.
Trent Mick 00:28:59 Okay, that's…
Daniel Dyla (Dynatrace LLC) 00:29:02 Is this rock big?
Trent Mick 00:29:04 You put me in my spot here. Just, I'll move on.
Marc Pichler (Dynatrace) 00:29:08 One of you also have,
Pranav Sharma (Google LLC) 00:29:11 I just… yeah, yeah, I just wanted to let folks know that this is actually deriving a lot of its content from a similar skill that was added in the Python package. The reason why it's so big is because it goes through, both greenfield and, like, brownfield, import of the open inference donations. So, like, if you already have some, instrumentation for a package that was donated by Open Inference, it, tries to import only the things that were not initially added in the instrumentation that already exists in your library. So, that's what made it a little bit bigger.
Marc Pichler (Dynatrace) 00:29:57 Okay, do you, do you know how… far along the donation process is in Python yet.
Pranav Sharma (Google LLC) 00:30:06 I think they're still, going through it, like, little by little, but I don't know when that effort actually began, although it would be easy to find out, because they're also using a similar tracking bug as us, so we can see when that tracking bug was created and how many things have been voted over already, so…
Surya Teja 00:30:26 Yeah, from the Python side, I can add a little bit more. Sorry for cutting your Pranav.
We started this around a couple of months ago. Open Inference, donated their piece of instrumentation, and on the Python side, we bought parity for Frontier packages, like OpenAI, Anthropic.
OpenAI agents.
And, then we started adding, right now, we are adding instrumentation support for Crew AI, small agents, and, Llama Index, which are, the agent frameworks.
they are going to get completed probably in next couple of months. So, Python will be in parity with Lama Index in next couple of months.
Marc Pichler (Dynatrace) 00:31:13 And the skill was useful in migration, so I guess that's why it's being added. Okay.
Surya Teja 00:31:19 Yeah, the skill was useful in migration, and also, adding on top of it, this skill will be helpful because the, inference and agent space is evolving quite quickly, and It is helpful in, shepherding codecs or Claude or something to implement it in a way where we are not breaking the existing ones, and we are taking care of the evolving ones.
Marc Pichler (Dynatrace) 00:31:47 Sounds good.
Alright, then I will, have a look at that. I will look into, the similarities and differences between that and the Python one, and, If it's, useful, then I think we can just merge this and, unblock you on that.
Surya Teja 00:32:07 Yeah, if folks are interested, I can add the skills from Python that we wrote, so that you can take a look and compare what we are teaching the agents, and you can suggest based on your findings from TypeScript also.
Marc Pichler (Dynatrace) 00:32:22 Yeah, I think it should be fairly easy to find, they would just be in the same folder, so I'll, would just, link the folder on a comment, I think that would already have a lot.
Trent Mick 00:32:35 The PR description already links to the equivalent Python skill.
Marc Pichler (Dynatrace) 00:32:39 Yeah.
then I think, there should be no action necessary. We can just have a look at that and see if there's… Anything that, we need to adapt, I mostly review this from the perspective of, like, how we usually structure packages and stuff like that, I trust that, the contents… From the, gen AI instrumentation sites are.
correct there.
If anybody else wants to review this, Based on that, please feel free to go ahead and add your comments there as well.
Alright.
Any questions or comments about the open inference migration schedule?
If not, then we can move on to the next one, which is…
Trent Mick 00:33:52 Another long essay from me, yes.
Marc Pichler (Dynatrace) 00:33:54 Yeah.
Trent Mick 00:33:57 Okay, so, like, over a month ago, Matt.
Who has joined now.
open this PR to add support for.
Config provider, which is another part of the declarative config, spec.
Which is great.
And I strung out and finally started reviewing, spent a bit of time on this. So, I pushed a… branch with a commit that I have that has quite a number of changes to this thing, but, basically going over some of the design decisions that you were forced into, like, the hell that is how instrumentations are instrumented and… or are created and started is, kind of a sore point right now.
Sorry, not a sore point, but it's just kind of a… design nightmare, I think.
So yeah, mostly, Matt, I only… put this up yesterday evening, so, I don't know if you've had a chance to look at it. I wonder what your thoughts are.
And other people having reviews, too, would be great.
As always.
Matthew Wear 00:35:03 Yeah, I did look over it this morning, and I think the… The biggest changes I'm seeing, and tell me if there's more that I'm missing, is, kind of the… the config properties change, you simplified it to kind of be these tuples, rather than kind of the I don't know, the heavier Java-looking machinery, where you kind of Good.
get string, git boolean, get string array, on something. So, that simplified things quite a bit, so… So yeah, I think that's… that's fine. The other thing that, that I'm still unsure of, is that this… even my initial implementation, I guess, was missing, Yeah, Jackson reviewed my initial implementation, and my applying of the config was a little bit too late. It was happening after super, which happens after init and enable.
And, And this is happening… even later than that, so I think that's… I guess the biggest thing that I really need to clear up is, like, when does the declarative config need to be, available? And ideally, it would be available to all of those things, and I do see that there are some… instrumentation that do read their config in init, so, having the declarative config not be available there is not great.
But I feel like that's a bigger… maybe a bigger issue with just how instrumentation gets set up and enabled.
Trent Mick 00:37:00 So, yeah, so here's… here's my understanding of things there. So, And this possibly requires changes to instrumentations.
the… a thing that helped clarify for me a little bit is there's a… there's an open PR right now… On… on the spec, I think. I have to go find it, and I can link it.
to add support for, and in fact, it's gonna be the next… I was asking for an opinion, the next bullet point for this… the agenda for today.
To add support for, dynamic configuration changes, so that an instrumentation can register, a handler callback.
for when… the declarative config, or a section of the declarative config changes. This is setting up so that, for a thing called… policies in OTEL so that remote configuration from an op-amp server can send new config to a running SDK.
And then how does that config get to the various instrumentations? And so the proposed mechanism is that the instrumentations can register a callback to be notified when config changes. The thing that helps me clarify here for this is that an instrumentation to support At least to support changing configuration, needs to… Not change how they set up based on configuration.
In that the changeable configuration is something that you change on the fly, so subsequent requests or… things that touch on the, like, monkey patching instrumentation that you've done uses that configuration, but the initial setup isn't changed by that. So, to me, this, this, instrumentations that currently use their config.
in the init step, so this is during construction, or very early in their stage, may have to change away from doing that, and that they have to set up so that they get their monkey patching hook in the library that they're instrumenting.
But then if, like, the sampling rate changes later, or that's a bad example, but if, you know, they're enabled or disabled later by remote configuration, then they aren't going to remove their hooks, they just… act as no ops in that case, or if some other configuration item changes. So, for example, if which… client response headers should be captured by HPP instrumentation. That's information that has to be able to change dynamically on the side. So, to me, having the declarative config stuff applied to instrumentations at construction time doesn't need to happen that early. It can happen a little bit later.
The… the major problem that I'd had is that right now, we didn't… We don't have so… For non-native instrumentation, so for instrumentations that are set up by the SDK, we call this register instrumentations function.
There… we don't currently have a signal to instrumentations that, like, okay, the SDK's set up, we've got the providers.
You can use them now.
The assumption and… A little bit by the spec, though I don't think it has… Our normative language on this is that A instrumentation that gets a tracer from the tracer provider.
We have these proxies set up so that, If the SDK later registers the proper global tracer provider, the tracer that the instrumentation already had should Be wired up to that new one that came later.
That obviously doesn't work for config, so an instrumentation can't start up, get config from the config provider, and then later the SDK adds config information from the YAML file that it's parsed, so it's already too late, so… This kind of felt like one of those first points where we needed a signal to tell instrumentations, okay, yeah, it's ready, it's there, you can go grab it. And so, Anyway, I'm not sure if I answered your question, but I think, like, I'm not as worried about… And I don't think we can have, Instrumentations assume that they're going to be able to get the declarative config stuff at construction time, so… this changes it to be a little bit later. And it… it does mean that I think we should write some docs about what the expectations are around config, and how instrumentations that are starting… that will opt into getting this declarative config will need to possibly adapt.
To that, if that's clear.
Matthew Wear 00:41:52 Yeah, yeah, I think the key takeaway is there's… there are some issues there, but… Don't worry about it, we're going to solve them other ways, is… Is what I'm hearing. And I think it's not, like, an epidemic. I think there's only, like, a handful of instrumentation just at a scan that, does access its config earlier on in the lifecycle, so I think changing that is… is doable.
Trent Mick 00:42:23 Did you… do you possibly have a handy list of those, or can you reproduce that search? Because if we… if you can post them as a comment, then I'd love to do a sanity check saying, like, oh my god, it would be really bad to make this design call, but I don't think it will be.
That hard-to-adapt existing ones, but…
Matthew Wear 00:42:40 I, yeah, I can, I can do a little more research, and if I get a short list of known ones, I'm not gonna probably claim that they're all of them, but definitely, We'll verify that they… they are offenders. I'll… I'll… I'll post that somewhere, and… And yeah, I don't know, for, For everybody who has not really looked at this, like, I don't know.
we don't need to spend a ton of time on this, but I feel like the biggest change is maybe, if we… wanted to look at what this PR has.
for, like, the HTTP instrumentation, how it uses the declarative config, and then kind of look at your branch, how it uses the declarative config, that might just be, like, a quick A-B that we can show to people to see if… Boom.
If anybody has opinions.
Trent Mick 00:43:36 I put a link to how the… one of those links, Marc, I don't remember which one, so I think so that's… So, yeah, one of those bottom two.
Probably…
Matthew Wear 00:43:53 Brought with some stuff in the chat.
That one would be the… It's a new way.
Trent Mick 00:44:14 Did you follow Matt's link?
Marc Pichler (Dynatrace) 00:44:17 R.
Trent Mick 00:44:18 in… in…
Marc Pichler (Dynatrace) 00:44:19 This is the second one that I clicked at, one second… I'll just need… My chat window has disappeared.
There it is.
Alright.
Matthew Wear 00:44:37 And here's the second one, I guess.
Those links do anything.
So yeah, this is kind of how… how it is today. I guess how that would work is that you have, Yeah, I guess the config provider is kind of nested below this helper here that, Is a… a function that you, that you pass to Super, I think it's called at the right Right place. And then, the first link that I posted in is… Trent's reimagination of this.
Where it…
Trent Mick 00:45:27 Okay, it was…
Matthew Wear 00:45:30 Right.
Trent Mick 00:45:30 Yeah, that's that config… set config provider. Line 203.
Matthew Wear 00:45:36 So here you have these, tuples… That kind of map the, the… Dixon?
Trent Mick 00:45:46 The mechanics of the helper are…
Matthew Wear 00:45:50 And then a config property.
Trent Mick 00:45:55 The, the mechanics of…
Marc Pichler (Dynatrace) 00:45:56 -
Trent Mick 00:45:56 To help her, so yours apply.
what's called ApplyDeclarative Config, and this one's called read config properties. I think… is a little bit independent of what the main issue… the main issue here is whether The stuff is being used at construction time of the instrumentation.
Which would require a change on how instrumentations are passed in. You have to pass in an instrumentation factory into Start Node SDK versus the already constructed instrumentation.
Versus a set config provider being added. This is para… on the instrumentation class. This is in parallel to the setTracer provider, setMeterProider, set logger provider.
Marc Pichler (Dynatrace) 00:46:36 Oh, we already have.
Trent Mick 00:46:38 Yeah.
Marc Pichler (Dynatrace) 00:46:41 So you're saying here, the… where the config is to be obtained, and then you have the type.
And where it's supposed to go, right?
Trent Mick 00:46:51 Right.
Matthew Wear 00:46:55 Yeah, so this is just from the perspective of the instrumentation, I guess, that… how this works. And then, yeah, the other… This was kind of… the… I think the first change that I mentioned, and then the second change is… is the bigger change.
is, like… at what point in the lifecycle do we actually set up the declared config? In my PR, I went through a lot of, effort, I guess, to be able to make that available in the constructor, but it, yeah.
It's… It requires a lot of changes, and it doesn't really work with, previously… initialize instrumentation, and it kind of sounds like Having declarative config available at construct… at construction time is not really something that we necessarily want or need.
Marc Pichler (Dynatrace) 00:47:52 You know, the only thing that… I think where this would be necessary is, for example, I think there's an option in Instrumentation HTTP where you can… Avoid patching the server part of the library?
That would need to be… Available at least before patching.
Matthew Wear 00:48:24 So that's before Annette, which is… Which is before… Which is really construction time, which is kind of… It's not… it's not impossible. I mean, this PR demonstrates that it is possible to have declarative config available at construction time. It just requires that you're, it just requires that the Node SDK gets an instrumentation factory, and not, like, a list of registered instrumentations, which is what it gets today.
So… It's… It's possible, and this PR is proof of concept of that, but it is a change, and it seems like a change that We may or may not want.
So…
Trent Mick 00:49:13 What is that… Don't repatch certain things.
Disable incoming request instrumentation?
Marc Pichler (Dynatrace) 00:49:23 I think so, yeah.
I think it might be… Yeah, one of these two.
Trent Mick 00:49:36 So… maybe this ends up feeling more controversial, but I don't think we should be… In the same vein that we've talked about not having unpatch support in these things, because that's just fraud.
I think an instrumentation that's doing its monkey patching should… I've selected the HP instrumentation, it's gonna put its fingers in.
And then there's config that can be updated later.
That decides whether Those hooks are gonna do anything.
So I guess I… I'd argue for the one… maybe this is the only example that we have. HP might be the only example where it wants to use its… constructor.
options to decide which monkey patches to be putting in. Or another option would be to have HTTP client and HTTP server separate instrumentations, and people can select which of those instrumentations to use if they don't want to use You know, hooks on one part of it.
Marc Pichler (Dynatrace) 00:50:40 Yeah, makes sense. And also, we don't have to support all the options.
Trent Mick 00:50:46 That's… that's true, yeah.
Matthew Wear 00:50:50 Cool, yeah, so we spent some time on this, I don't want to take up too much more of the meeting, so I'll… I'll try to come up with a list of things that, use config.
early in the life cycle, just so we know. And then… if it's a small list with options like Trent was suggesting, where, It's… Yeah, it has con… like, it will set up the hooks, but it will read the config, you know.
Yeah, it will set up hooks during patching, but not necessarily use the config there, and use the config from the hooks, approach, if that is… Something that will work for all those instrumentations, then that should be kind of our guidance, and then… all this stuff to kind of, move the clarity config further up in the lifecycle is unnecessary, and then… yeah, I guess if anybody else, as a result of these discussions, looks at this, has some opinions, just please comment on the PR so that I know what direction to start taking it, but… But yeah, I'm… I'm fine with all of the, suggestions that you have, Trent, and we'll kind of start working in… In that direction, and… boom.
Trent Mick 00:52:05 You could… you could certainly take my admit. I'm not sure if you… Or I could push it to a separate PR.
or, like, or create a PR from that… from that branch or not, I don't know what's… What's easier there?
For now, I'll leave it, and you can comment, let me know.
Matthew Wear 00:52:23 Cool, yeah, I'll… I'll look at it and let you know.
Marc Pichler (Dynatrace) 00:52:28 Huh.
Thank you.
Alright, I guess let's move on to the last two topics here.
The first one by, Pranav.
Yeah, the Gen AI util package that we talked about last week.
Pranav Sharma (Google LLC) 00:52:47 Yep.
Yeah, this is just to, request… for reviews, and just wanted to know, like, I know this PR is pretty big, and based on our last meeting, I did make everything experimental, and this package right now does not export anything. So, as we discussed, as the library instrumentation's use.
public functions from this package, they'll keep on exporting stuff, but I just wanted to know if the maintainers would actually be okay in approving a PR of this size.
Even if it's experimental. I just wanted to, do what I can to speed up the review process, so just, seeking advice here.
On how the community feels about it.
Marc Pichler (Dynatrace) 00:53:34 Yeah, it does feel a little large. What we've done in the past is we have merged, like, skeleton packages, where it's… it was… or the boilerplate, first, like, the package JSON, the license file and everything, just to get that out of the way, and then, we started merging in the actual code.
To, like, reduce the diff a little bit. That's something that you could, definitely look into.
Okay.
Go.
I have had a look at this, the way that it's structured right now, it seems to make sense to me.
one of the issues that I'm having at the moment is, just… I don't have enough insight yet into, like, how the… packages look like that we are instrumenting, so it's a bit difficult to make a decision on whether the code that's being merged Is actually, matching up with what we're instrumenting.
So that creates some friction. But, yeah, if we can split it up somehow, that would be… Would be appreciated, then… I think we can make some additive changes to it.
Rather than going with one large PR, which might drag on in the review section.
Pranav Sharma (Google LLC) 00:55:10 Okay, alright, I can then try to split it up based on, like, functionality.
Alright, yeah, mostly just was a call for reviews, and thank you for your advice. I'll take a look into it, yeah.
Marc Pichler (Dynatrace) 00:55:25 Thank you. One question, I saw the… issue about the GenAI semconf, That should be mostly reserved with the PR that's opening core, right?
Pranav Sharma (Google LLC) 00:55:40 Yes, I looked at your comment, and I think you were right. This was mostly duplicative. I did not look into the issues for OpenTelemetry JS. It was opened against the JS repo, not the contrib one. So, but yeah, you're right, it should be covering my concerns as well.
Marc Pichler (Dynatrace) 00:55:57 And it will probably also… Cover this file here, right?
Pranav Sharma (Google LLC) 00:56:03 Exactly, it should go way down, yeah.
Marc Pichler (Dynatrace) 00:56:06 Alright, sounds good. Then that would also probably reduce the diff quite a bit, so that's good.
Pranav Sharma (Google LLC) 00:56:12 Yep.
Thank you.
Marc Pichler (Dynatrace) 00:56:14 Alright, thank you.
Trent Mick 00:56:17 That's 7,014 you're referring to?
the GenAI Semantic Conventions package?
Marc Pichler (Dynatrace) 00:56:23 I think so, yeah. Sounds about right.
Trent Mick 00:56:26 I had a link in chat.
Marc Pichler (Dynatrace) 00:56:27 - My check window disappeared again. One second.
Yeah, exactly, that's the one.
So we'd probably need that first, to unblock the other one.
Planning to do a release soon as well, in the car repo, so… Or make sure to get that in elsewhere.
Pranav Sharma (Google LLC) 00:57:06 Any, any idea on tentative, date when this might go in?
Marc Pichler (Dynatrace) 00:57:13 So for this PR, I'm not sure. I'm hoping to get the release out before September, like, before the 1st of September, because that's when we are… Scheduled to start with SDK 3.0.
This one's.
Trent Mick 00:57:27 still in draft, though, right?
Slow.
Marc Pichler (Dynatrace) 00:57:30 Yeah.
I think there's…
Trent Mick 00:57:32 reviews.
Marc Pichler (Dynatrace) 00:57:34 I think there's not much that needs, adjusting.
I think it was just opened as draft, I'm not sure if, Workgang has…
Trent Mick 00:57:46 And there's still a CLA issue to sort of…
Marc Pichler (Dynatrace) 00:57:49 Sure.
But it should be fairly easy to fix, I think it's just because, claude did the co-author thing.
Alright, there's only 2 minutes left, sorry, Surya 2… Cut your topic short.
I guess this is also a car for reviews, right?
Surya Teja 00:58:23 Yeah, this is for reviews, actually.
I was not sure if, we should be sending the GenAIA utils first, and then port this, but, we tried stacked PRs in Gen AI folder. If you guys are fine with it, I can add this To that stack, and when that goes… we can add… we can later merge this, but I just don't know what the appetite is here, and just want to see what people feel about this.
Marc Pichler (Dynatrace) 00:58:57 you mean the instrumentation in general, or, the staked PRs?
Surya Teja 00:59:03 Yeah, the instrumentation in general, the instrumentation in general. Do you feel… I mean, you might be doing repetitive work because, this is going to, again.
be written in Gen AI Util's format.
So… are you fine with sending this and releasing it, and once when the Janaya utils… is ready, again, ported using GenAI utils. Is that fine with you, or do you want to wait till that is merged?
Marc Pichler (Dynatrace) 00:59:32 If this is already in the format of Chain AI Gutierrez, then I think it might even be easier to review this one first, and then review or refactor, that… like, just uses the GenAI utils later.
So…
Surya Teja 00:59:49 Okay, so…
Marc Pichler (Dynatrace) 00:59:49 I'm generally positive on, taking, or, like, looking at this PR and getting that in.
And then doing the reflect on it.
Before releasing our offline.
Surya Teja 01:00:07 Yeah, so this is not in Jennautils format, so I'll leave this as is, and once Jennautils is ready, I'll port it as we have another PR for… already a PR for that one.
So, did I… did I understand you correctly?
Marc Pichler (Dynatrace) 01:00:22 Yes.
Surya Teja 01:00:26 Thanks, Mark.
I'm done.
Marc Pichler (Dynatrace) 01:00:34 Right?
We are finished right on time. Thank you, everybody, for joining.
Have a nice week, and… See you next week. Have a good trip, my dear.
Jackson Weber 01:00:47 Yep, have a good one.
David Luna Bistuer 01:00:48 Okay.
Marc Pichler (Dynatrace) 01:00:49 Bye.
