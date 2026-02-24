SIG: Browser SIG
Date: 2026-02-19
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/5y1hRo1z3-PBzp5DmfjDSmK5Cz8mhdWno_KaVK0x-fHmyNAb27ZJgk01Sd24tjbd.KJJLABBQhJddtGyv
============================================================

## Zoom Recording Transcript

**Benoît Zugmeyer** 02:24 Yo.
**Joaquín Díaz** 02:26 Alright.
**martinkuba** 03:53 Can you all hear me okay?
I wasn't… I couldn't hear any sound, so I wasn't sure.
Can someone say something?
If I can hear you.
**Ted Young** 04:05 Yo.
**Joaquín Díaz** 04:06 Nope.
**martinkuba** 04:07 Okay, cool, I can hear you.
Okay.
**Ted Young** 05:09 I see that what I was putting on the agenda was the same as what Carlos had put on.
But I don't see Carlos.
**martinkuba** 05:38 Alright, it's 5 after. I think I started. Oh, here's Carlos.
Okay, so I have the… I have the first topic.
Share my screen.
So… Last week, so I created this… this issue.
A while ago, maybe a month ago,
Basically, we need to get it to a state where we can do a release.
The first step, I mean, before we…
Build out some, some tooling around
releases and publishing. It's like, we need to decide how to do… how to have
how to manage our packages and how to manage versioning. I created this issue, and there's been some discussion on this issue. We discussed it last week, but…
This is actually a different group than last week. Jared was here last week, and…
He commented on this issue.
So, I can just give you, like, a quick, quick summary, and…
I would like to get to a place where we can make a decision as a group.
As, so… Yeah, so basically,
Right now, we have… we have,
Multiple packages in the browser repo.
For… for each… well, like, there's a separate package for each instrumentation.
And then, so we were trying to decide, like, should we have them versioned independently? Should they have, all the same version and be released all together?
basically two models, like, there's one model, like, in the JS Core, there's a different model in JSContrib. Jared brought up the… the third option, which would be to have a single package for… for… that would contain all instrumentations, and we would… we would handle…
We would handle the… the experimental to stable by, export subpaths. So, you know, anything experimental would be… essentially would be, exported as under experimental subpath.
It seems like there… there are, you know, a few people are in favor of this approach. It would… it would…
Definitely simplify the process, the release process.
It would also simplify the dependency or compatibility question.
So the… the proposal that seems to be kind of forming is… is…
There would be… We would have, like, one…
like, SDK package that would have…
the browser SDK-specific things in it, like a configuration layer, like session management, things like that, and then we would have a second package for
That would contain all the instrumentations.
they would be all the first-party instrumentations that we would maintain in this repository.
There is potentially a third… third package that, was, was suggested here to be, like, a distro, which would,
contain…
You know, some defaults, some recommended defaults for users, so they would… they don't have to install two packages and do, you know, manual configuration. They could just do it through one package.
So that's kind of where the discussion is on right now.
What I would… what I would ask…
folks in this group, like, if you… if you are okay with this approach, give a thumbs up. If you have some opinions.
Some other suggestions, please comment on this issue so we can move forward with this.
Any questions or comments?
**Joaquín Díaz** 10:08 No, I like the hybrid approach.
I guess my only concern is that
If all the instrumentation have shared dependencies,
If there is a breaking change on one of the appendices that is breaking another instrumentation, then…
You have to fix all this implementation at once.
I don't… thing that's going to happen a lot, but I'm… I… I'd rather have this been more…
User-friendly by being a single package than…
worrying about something breaking every now and then, so… I think it is fine now, I agree with the approach.
But just that comment, like, we have to be careful when updating dependencies, since they are going to affect all the instrumentations at once.
**Daniel Dyla (Dynatrace)** 11:05 The instrumentations should only depend on…
the API and the instrumentation base package.
So I don't think that that's likely to happen all that often. And I guess,
Depending on how you go, sometimes the instrumentations depend on that thing that they're instrumenting, but we've actually…
Been moving away from that.
So… I'm not sure how often that problem is likely to come up in practice.
**Joaquín Díaz** 11:37 Yeah, yeah, maybe… maybe Dennis Hopkins, but just saying.
But if…
So if, for example, if you are instrumenting, I don't know, Web Vitals, and you use the Web Vitals library.
so that dependency is a dependency for the entire instrumentation package, and only for the Web Vitals instrumentation.
**martinkuba** 12:02 That is true.
**Joaquín Díaz** 12:06 So that means that if you pull in the experimentations and you don't care about web vitals, you are pulling in the web vitals already.
I… Tank is fine, because it will most likely get too shaken, but, if anyone has come…
Verify that, or validate?
that is going to happen. I know Jen knows better.
about these things, so we can ask him later, I can ask him later. But that will be something to have in mind. But I'm sure it's fine, but, I would like to confirm that.
**martinkuba** 12:44 Okay, sounds good, yeah, you can…
**Joaquín Díaz** 12:47 I can add a comment here, if you want.
**martinkuba** 12:50 Yeah, that'd be great, thank you.
I also would have, like, in my comment here in the proposal, I do have some open questions that I think would need to be resolved.
But, yeah, we can… we can take that,
We can dig that offline, that's okay.
Alright.
**Carlos Alberto Cortez** 13:21 By the way, Martin, since you are already sharing your screen, maybe you can go to your item, and I can briefly talk about my stuff after you.
**martinkuba** 13:28 Sure, yeah, I think so.
**Carlos Alberto Cortez** 13:30 Thank you.
**martinkuba** 13:31 Any other comments on… Well, in the versioning.
Alright, let's move on to your topic, Carlos.
**Carlos Alberto Cortez** 13:42 You don't want to talk about…
longer fix for consumer instrumentation. First, probably. Mine can wait, definitely.
**martinkuba** 13:50 Let's just try to open the first link?
**Carlos Alberto Cortez** 13:54 Sure.
Thank you for that.
So, basically, this is a set of PRs regarding, entity that it would be great to have, you know, some exercise from the browser tick.
I would say, especially this one, Daniel Daylight…
who's in the code also, he wrote a prototype in JavaScript.
So hopefully this should help, you know, on that front.
I know that having multiple resources.
Has been especially useful, has been something that has been requested in the past.
from any sites.
of the…
of the community, so it would be great to have ice. And you can see in the small description how it could look, like, you know.
Okay, we can go probably to the next one.
Please, yeah.
Like Johet.
**Ted Young** 14:55 I was gonna say, that last one, though, we were specifically asked if we could provide feedback on it, because it's so relevant for the browser SIG.
Josh Sirrest asked if we could…
specifically have a look at that one, so I just wanted to add that.
**Carlos Alberto Cortez** 15:12 Yeah, definitely.
The next two, like this one and the one after, are optional, but it also would be great to have you, you know, your eyes on that one.
This is for, entity detectors merge algorithm.
This, algorithm was already, described in data tips that has been merged already, and it has been tested.
So it should be fine, and it's in development status.
But still, it would be great to have eyes on this one, you know?
And finally, if you could open the last one, that would be great, yeah. Likewise, this is also based on some
a tab that has been merged. This is regarding adding, you know, adding events.
Regarding entity… entities, and it could be great to have also, your feedback. It's less important than the first one, but it still could be great, so if you have extra cycles, please take a look. As I said before, this PR is also based on, OTEPs that have been merged.
So, yeah.
It's, something we would like to, you know, to see, making progress slowly, yeah.
Yeah, actually, a lot of… yeah, go ahead.
**martinkuba** 16:33 Yeah, so it's essentially, like, for some part of the SDK, like, emitting these types of events.
**Carlos Alberto Cortez** 16:43 And to be fair, there's a lot to discuss, and actually you check, you know, the… the chat happening there. There are many things being discussed about here, there, details.
But it could be great that since this is still happening, people here review that, you know?
So we get the feedback while everybody's talking, you know? We are all aligned, yeah.
And just going back to what Tev said, the first one is the most important one for now, but yeah, it could be super good, this one, exactly.
As I said before, Daniel Dayla also wrote a prototype.
So hopefully that should, you know, help people here.
Would be really, really appreciated.
**martinkuba** 17:28 Daniel, the prototype that you've been working on, is it in a state that we could, test it with?
web browser.
**Daniel Dyla (Dynatrace)** 17:36 Yeah.
I, I think so.
It's not obviously published anywhere, so… To get it…
You know, working together, you probably would have to pull in my changes and run it from, like, a local
learn a repo or something like that, but I'm sure it would work just fine.
**Carlos Alberto Cortez** 18:01 And it's linked by the end of this PR, that's the last comment currently, I think.
probably we should do the edit, George comment description, so we know what the prototypes can be mentioned in the…
in the PR description, so we don't have, you know, people don't have to be going around trying to find us.
Sweet, that's all from my side. Yeah, it would be really great to have your eyes on that one. Thank you so much.
**martinkuba** 18:33 Is there… is there any specific part of this, or anything that you're looking for feedback on, or…
And it thinks, like, we should be… Like, specifically paying attention to?
Or just in general?
**Daniel Dyla (Dynatrace)** 18:49 I… I would say that, the…
If you go back to the PR and look at the PR description, I…
They're, not… yeah, not the…
Not this one, the… the… yeah.
So this, like…
for entity, so the idea is that you bind, like, an entity to a meter provider, or a logger provider, or a tracer provider.
It merges that entity into the resource that's already on the provider that you're binding, and it returns a new provider.
And then you're responsible for the life cycle of that, so, like, shutting it down and acquiring a new one when the entity changes. I guess that's the main thing, is making sure that that works. So, like, when the session ends or restarts.
Is… is the shutting down of the provider and creating a new one and reacquiring
loggers and meters and such from it. Is that a problem, or does it work?
yeah, that's what I would mainly focus on, is, like, the API itself, more than
like, the SDK internals of how that API is implemented.
**martinkuba** 20:24 Do you have… do you have any, like, an example of… of… in JS Core, how it would be, like, where…
That would be exactly used.
So, I mean, for us, for us, I'm assuming…
We register, like, a trace provider, log the provider, and then, like, the browser SDK would be managing this swapping of the providers behind the scenes.
**Daniel Dyla (Dynatrace)** 20:48 So there's only one global provider, and then the instrumentation, would acquire… a new one, by…
using the for entity method on the global provider from the API.
It would not swap the global provider, though.
**martinkuba** 21:11 Okay.
**Daniel Dyla (Dynatrace)** 21:18 That prevents instrumentations from interfering with each other.
**martinkuba** 21:24 Okay.
Right, yeah, I'll take a look at this and… Try to see…
**Ted Young** 21:30 lots of words.
I think it would be really helpful both for us and the entity SIG, for there to be, you know, a way to just clearly demo
Using…
**Daniel Dyla (Dynatrace)** 21:41 Yeah, an end-to-end use case.
**Ted Young** 21:44 You know, one thing in particular I think we want to pay attention to is, you know, the case where the session you're trying to track is across a lot of quick browser reloads.
Right? Like, that, to me, is where, does the way…
this API wants to handle shutdown, work well with
What we're trying to do with, you know, flushing things or getting things out the door.
But… to me, that's like… That's kind of one of the special cases around sessions and browsers, is…
Moving quickly across pages.
So, to me, like, if we saw it working well there, that would kind of indicate that…
It's gonna work for our purposes.
**Joaquín Díaz** 22:28 Do we have a definition on a session? In the browser, like.
Each tab is a new session, or multiple tabs are the same session.
I guess that's the questions I will try to answer, because that means
Well, for sure, every time that you refresh a tab, you get a new session object.
That needs to be added to…
provider, right, using this four-entity API.
By then.
If multiple tabs share the same session.
You have to think a way of sharing that across multiple tiles.
**Daniel Dyla (Dynatrace)** 23:09 Yeah, so…
If you share the same session across multiple tabs, as long as the entity identity attributes match, it should be okay.
The meter itself for the logger wouldn't be shared across multiple tabs, obviously.
But… Yep.
It's, you know, aggregating it from multiple tabs the same way you aggregate data from multiple different processes or different servers on a backend.
should.
Theoretically work the same way?
Where it's all just aggregated on the back end.
I guess the definition of…
A session is not entirely clear to me.
Like, is a session… If I refresh the page, have I started a new session or not?
Like, if I open multiple tabs on, you know, GitHub, for example, is that all part of one session, or are those parallel sessions?
I think we need to decide…
Because, like, in the most restrictive case, you could say a single
Page view is a session, and, like, in a single-page application, you may run through multiple
Pages of that, but then when you hard refresh.
that could be a new session. We could decide that that's the definition, in which case…
you get a new session ID and everything, this would definitely work.
If it needs to be shared, like, if you refresh the page, or if you open multiple tabs and you decide all of these are the same session running in parallel.
then… I believe it's still okay, as long as you can still…
guarantee you're getting the same session ID when you… Define the entity.
But then if you have descriptive attributes that you can't guarantee are the same, that may conflict.
That's where it might become more challenging.
So I guess we have to decide
what is our definition of session? And I haven't seen that written down anywhere yet.
**Joaquín Díaz** 25:30 Yep.
**Ted Young** 25:33 And I think the relevant thing here is, like, we have a session manager that would encapsulate all of that state.
And we kind of want to keep the session manager, in a sense, away from the SDK, right? The session manager, I'm imagining, is updating the entity provider and managing that bit. And as things are changing.
through the entity provider, that's updating the SDK in kind of a generic way.
So it's not that we would have to completely figure out exactly how we want session management to work by default, and also what kind of controls we want to give end users, because probably they're going to want to get fussy about sessions.
But what we want to know at this stage is, like, for the different kinds of ways we'd want to drive sessions, does this, like, entity manager and SDK work? Or is there some mismatch happening there?
That's making things difficult.
So, it would be helpful to be able to demo some of these more… these different, kind of, like… it seems like we're kind of at that point, right? We're demoing a couple different ways of managing sessions.
would help us… At least be able to give a thumbs up and get this layer stabilized.
Does that seem reasonable? Joaquin, I feel like I cut you off by accident.
**Joaquín Díaz** 27:11 No, no, that's fine. Yeah, I think that makes sense. I think…
if the API makes sense for the browser, then…
Knowing when a session starts is a different conversation that we can have later.
Yeah.
**Ted Young** 27:27 But it's like, to manage that, you would be interacting with various, like, browser storage systems and their APIs for when you can, like, grab that data and put it back.
**Joaquín Díaz** 27:36 in.
**Ted Young** 27:36 Right? And then this thing… you have to be able to, like, feed that into entities and have that update all the right SDK components and not have weird…
Not have something about that get weird, right?
So I think that's the thing we want to prove to people. There isn't some weird interaction going on between that whole chain of APIs.
**Joaquín Díaz** 28:01 Yeah.
**martinkuba** 28:12 Okay, we've got 2 minutes left, anything else on this?
Very cool. I have just one more thing that I… we don't have to discuss in detail, but Daniel, since you're here.
We talked about this diagnostics logger.
A few, few weeks back.
And I, I opened… to,
two PRs to address the… address it,
If you have a… if you have a… if you have time and preference on which one to…
move forward, so I would appreciate feedback on that.
**Daniel Dyla (Dynatrace)** 28:49 Yeah, okay, I'll take a look at them. I've been…
essentially on vacation since that meeting, so I'll… I'll try to catch up a little bit. These are two…
competing PRs, they're not… wouldn't merge both of them, you'd merge one or the other, I guess?
**martinkuba** 29:07 Correct, yes, yeah. I think one of them is based on your suggestion, and the other one is based on Mark's suggestion.
**Daniel Dyla (Dynatrace)** 29:15 Got it. If that's the case, then…
Usually, Mark knows what he's talking about, but I'll take a look.
**martinkuba** 29:22 Cool, thanks.
Alright, anything else? We're out of time.
Cool.
Talk to you later, everyone.
**Daniel Dyla (Dynatrace)** 29:36 Thank you.
