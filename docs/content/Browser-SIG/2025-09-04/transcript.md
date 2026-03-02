SIG: Browser SIG
Date: 2025-09-04
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze (embrace)** 00:46 Hey, what's up, everybody?
**Martin Kuba** 00:50 Hello.
**Ted Young** 00:53 Hello, hello!
**Jared Freeze (embrace)** 00:55 Welcome back.
**Ted Young** 00:56 Yeah, gonna be back.
What'd I miss? Anything crazy?
**Jared Freeze (embrace)** 01:10 I'm just trying to keep moving.
**Ted Young** 01:17 All right, well, feel free to add things to the agenda if you have not already.
And… add yourself.
As an attendee.
I'm not there.
Alright, I'm just gonna pop one FYI to the top.
The agenda, which is just about becoming a GitHub org member. We got some…
some new people in the SIG, and I'd love to start assigning you issues and things, and in order for any of that to work, people have to become a member of the GitHub organization. It's really simple, the only real requirement is we ask, that you
find two sponsors, and then you open an issue in the community repo. There's a template, I have a link to it in the meeting notes and on our Slack channel, just like a new membership request.
Fill that out, and then have your two sponsors respond to that by saying, I support.
And then you'll get added as a member. You do have to sign the CLA, the CNCF CLA, as part of this. There's sometimes a question about, do I sign this as, like, an individual, or as, like, sign the corporate CLA?
If your organization is not pushing you to sign the corporate CLA, it's a lot easier to sign the individual one, I will say that.
Which one is right or wrong? I have no opinion about.
And that's it.
So, if you're not an org member yet, please do that.
Cool.
Alright.
Let's maybe kick it off. Martin, you want to talk about semantic conventions? Page view?
**Martin Kuba** 04:08 Yeah.
So I've been working on the page views and at the conventions for a while. It's for the page view event.
And, made some changes to it, and, that I wanted to bring up to discuss here.
I also posted in Slack, so we can…
If you don't make… make a decision here, we can follow up there. But,
There are a few things that I wanted to point out,
First of all, we had the… the event
was called Page Underscore view in the past. There was a comment on the PR that said maybe we rename it to
Page.view.
I don't have, like, a strong opinion either way, but there is some precedent for
For example, like, for session, there's a session.start, And session.end.
Event already in the semantic conventions, so… kind of makes sense that maybe under… if we think of a page as a…
I guess, entity, or, then, like.
Page.view could be one of the events instead of page underscore view.
Again, I don't have a strong opinion here, yeah.
**Joaquín Díaz** 05:34 Makes this way.
**Ted Young** 05:36 I mean, I think it's a question of, like, do we see page as a namespace, right? Do we need an additional namespace with a bunch of other stuff? Or is the namespace browser? And then the browser named all these events, we didn't name any of them, we're just using their name.
**Martin Kuba** 05:52 Yeah, so…
**Jared Freeze (embrace)** 05:53 dot, you know. Because if we change our mind about title, we're gonna… then we're gonna have page underscore title, and we're gonna wish we had page.title.
**Joaquín Díaz** 06:03 I think there are many things that may fit into the page namespace eventually.
So, yeah.
**Martin Kuba** 06:11 Yeah.
**Ted Young** 06:13 Yeah.
It's just, in the browser, the event is called page underscore view, right?
Or no.
**Martin Kuba** 06:22 Oh, sorry, where?
**Ted Young** 06:24 I'm just curious, in the… like, is the browser calling it Page?
Underscore view.
**Martin Kuba** 06:32 There's… there's, like, nothing in the browser API that's… that even talks about page or page view, so…
It's a made-up event, and I was actually…
**Ted Young** 06:41 up stuff, okay.
**Martin Kuba** 06:42 Yeah, but the page view event is…
It's the concept that we came up with, so…
**Ted Young** 06:49 I see.
**Martin Kuba** 06:52 But yeah, one thing that I've been realizing, and it's, like, maybe it's obvious to everyone else, is in the past, like, when we…
thought about…
I was… I was thinking about this more like a telemetry model, rather than, like, a data model for browser.
Like, where, like, we would just capture, like… so we… we had, like, this list of events, and before we switched to… from body fields to, like, registry attributes.
You would just have, like, a list of…
Like, fields that are just basically make sense in the scope of the event.
But now that we're, like, moving to…
Using attributes, like, we already have to think about modeling more.
So, like, what kind of things…
what makes sense as a namespace that we want to reuse in different events or different parts of the telemetry. So, like, page and navigation may be our namespaces that we'll want to think about some more.
Yeah.
Okay, so I made… make… so this one is… we'll keep it as page view.
for,
The… the other one… the other… the next thing that I wanted to talk about is the title of the page. It was something that was originally proposed. There was a comment that said.
That, you know, it's… this could be potentially problematic for instrumentation because of PII information.
Could be in, in the title.
Also, it's high cardinality… cardinality,
attributes, so… I don't know, and I honestly don't know, like, how useful it is to capture page title.
So we could remove it for now and just edit later, but I was… I wanted to hear, like, what others think about capturing page title.
**Jared Freeze (embrace)** 08:42 I don't think it's any more or less sensitive than 4-string cramps.
you know, sometimes people use page title in lieu of changing the URL, like in SBAs. Sometimes it's the other way around, where the title's always the same, and the
URLs change, so… I don't know, it's of limited value right this second, I would say, because you might also have to parse it. People put their company name, and then a dash, and then something else, you know, it's…
It's a little chaotic, so maybe URL's just what we sort of hone in on, and then come back around, but as far as, like, PII goes, I think they're equal, to be honest. Because if you don't scrub it exactly right, like, you still might wind up with a token, or, you know, something… something very personal that just happens to be a folder name, so…
**Joaquín Díaz** 09:28 What's… what's the idea of adding the title list so people will kind of, like.
Identify the event, or relate it to a page.
Or why do we need a title?
**Martin Kuba** 09:40 Yeah, that's my question. Like, do we… do we even need it?
**Joaquín Díaz** 09:44 I don't think so, I think there are better ways to relate the event to a patient. URL is one… I think, eventually, I would like to have something that is, like, a route or something that is not the full URL, but the pattern that builds the URL.
So you don't have, like, the entire, like, cardiacity of having, like, 10,000 product IDs or something.
But for now, I think I will keep title out, and then maybe keep the URL until we have the pattern or the page ID or something.
**Ted Young** 10:13 I think this might be a…
Given that people are really concerned about bloat and payload size and all this stuff, with anything related to the browser, maybe we can take the approach of only
you know, it's a lot easier to add additional attributes later than it is to, like, take something away, so maybe we should be very conservative about what we add. Like, only add things because we have an intended use for this thing in our…
data model.
And to your point, like, Is our data model telemetry versus, like, a model of the…
browser, and it's, like, kind of both, right? Like, it's a model of the browser from the perspective of, I'm an operator trying to debug this thing.
**Martin Kuba** 11:10 Yeah.
**Ted Young** 11:10 So, I think just being clear when… whenever we add attributes, or events or attributes, just being super clear what at least one use case for this thing is, and if there isn't at least one super clear use case that we're trying to support, then we just don't add it.
And people can come back later and be like, can you please…
Please add this, and we can figure it out.
**Martin Kuba** 11:33 Yeah.
Okay, so I'll take the title out for now.
And similarly to that, we also have… this, push state…
Or, what is it called? Entry?
Let me see… Oh, state change, yeah, sorry, state change.
I… I wasn't… so again, like, this was… I'm kind of reviving this PR firm a long time ago, and I wasn't 100% sure the intent for this.
It seems to me like it was intended, like, to capture the, impact on the history.
whether, like, you know, like, so… but it's… the fact… even the fact that it's, like, the name is not clear to me, like, I think is… is a sign that, like, it either needs to be renamed, or we take it out for now.
We had… I had, I proposed, maybe changing that…
To be, like, a navigation type.
Oh, actually, that's, that's… sorry, that's, that's separate.
But it… yeah, there's… there's a navigation… navigation namespace that we want to talk about, too. But for… for…
this one…
I'm kind of thinking, like, maybe, like, if you don't feel like we… it's useful, like, we also take it out for now, because I'm not clear on…
The value of this.
**Ted Young** 13:12 And this is something we're essentially inventing.
**Martin Kuba** 13:16 Not exactly inventing, like, there is,
There's a concept of… of the… I'm like…
History effect, or the effect on history?
That I think might be useful eventually. So, like, I proposed here, like, navigation history entry change, or…
Something like that, to make it more… more obvious, but… .
**Jared Freeze (embrace)** 13:45 I'd like to echo, Ted. If we can't think of a use today, like, let's leave it out, right? I can't really think of one. I mean, if anyone else can put it forward, but I'd say we just drop it until it comes up.
**Dan Gomez Blanco** 13:59 Would that be specific to soft navigations, or…
**Jared Freeze (embrace)** 14:04 You can do window.location.replace, I don't think it's very common, but you can do it without…
SoftNav? .
**Ted Young** 14:17 Yeah. I mean, I can definitely see this is interesting information people want to know.
Potentially, but how you model it like…
You need a use case to understand how to model it.
From the perspective of, like, we're observing this thing, trying to debug it.
So I'd want that use case.
**Martin Kuba** 14:42 Okay, yeah, sounds good, like, we can probably take it off for now.
The last… and the last question that I had was, the event had a type attribute.
Which originally was just 01, to represent, like, hard navigation, as opposed to soft navigation.
I changed those to… to being, human-readable. So right now it says page load and soft navigation.
But… There are, if we're… if we're going to change… Like, like, one of the…
things that, like, I'm thinking maybe we should… we should rename this to Navigation Type, or something in the navigation namespace would make more sense than page view.
But with that said, there are…
I think multiple, like, definitions out there of navigation type.
So maybe, like, more discussion would be… would be needed here.
Like,
there is, there is the, the spec for… in the navigation API has things like navigation type, which has push, replace, reload, and traverse, traverse.
Options, which doesn't include the self-navigation, it's like a different, different concept.
Also, there is… there are other types of navigation, such as, like, potentially, like, forward-backwards.
Cash, like, like, replacing from cash.
Pre-render, things like that, so…
And then this is… this goes, like, the modeling. This goes back to, like, how we want to model this as far as navigation.
For the purpose of this event, we just want to distinguish, is it…
Is it, like the hard navigation or south navigation?
So I guess I'm trying to decide how to… how to go forward on here.
**Jared Freeze (embrace)** 16:48 So, I left a comment for four values that I think model what the user is doing. So, it's not about history management.
It's just about…
how the page is actually loaded. Like, what… sorry, what was requested by the user? So, did they reload it? Did they have a soft navigation, hard navigation? Did they use back-forward? I think history management is… again, I can't really think of a use case where I'd want to report that as leading to some answer.
But if we're thinking from the user's perspective, that would be… what I put forward.
**Ted Young** 17:24 Yeah.
I mean, I can certainly see trying to debug some kind of logic that only gets triggered in one of these cases with some
Finicky front-end framework.
That's, like, the first thing that comes to mind.
Some hook that runs on one of these kinds of loads, but not on the other one, and aha, that's where this funky behavior is coming from.
Only occurs when the user does this sequence of things.
**Martin Kuba** 17:56 Yeah.
**Jared Freeze (embrace)** 17:56 We actually… we already have a… I'm sorry.
**Joaquín Díaz** 17:59 No, I was just saying that I think that, in these cases, it's very useful to know, like, mostly the difference between, like, soft navigation and hard navigation, because on hard navigation, you reload everything, you get all the resources back and everything, so…
That is, you know, interesting to know when you're trying to finish.
**Ted Young** 18:20 Yeah.
That'll affect both speed, but then also with soft…
loading right, you end up with state carryover, right? So sometimes you can end up in…
Weird situations where state refreshes on a hard reload, and it doesn't on a soft reload, and that's… that's the source of your weirdness you're trying to get at.
**Martin Kuba** 18:42 Yeah.
Yeah, I think it's just more about the naming, like, what do we name this? Like, I don't want to override some existing term that, you know, people use for something else.
So…
And, like, the trick is also, like, soft navigation doesn't actually exist in the spec right now. It's, like, experimental everywhere.
So…
**Ted Young** 19:06 In the… in the browser spec, you mean?
**Martin Kuba** 19:09 Yeah, yeah.
**Joaquín Díaz** 19:14 I think that if there is no spec, We can…
Just use something that is easy to understand for everyone.
And I think self-navigation, or iron-star navigation, makes sense, so… I wouldn't, like…
think too much about it. I think if it makes sense, then it's fine.
**Ted Young** 19:37 And I would recommend just… just sticking with the current Page view name, also.
we can… We can review all of this stuff later, when we've got…
Enough of it up on the wall.
**Martin Kuba** 19:50 Yeah.
Okay.
**Dan Gomez Blanco** 19:56 Before we move on, I just had a question that I'm not sure if it was already discussed in the PR, sorry if I missed it. When we talked about this event as being, like, measure, you know, not containing any timings or anything like that.
And we basically have a separate event for that.
would you expect to have some of these attributes being duplicated into that other event? For example, the URL, referrer, things like that would be in both… both events.
**Martin Kuba** 20:24 Yes, yes.
Potentially, yes.
**Dan Gomez Blanco** 20:29 to be, like, I think… I'm not sure if someone mentioned that, like, the concept of, like, a page ID.
And to link them, you know, to join between… between them. And I think we didn't go for that approach, right? We're just duplicating the…
The attributes that we're interested in.
For the different events.
**Martin Kuba** 20:51 Yeah, I mean, we haven't talked about Page being, like, an entity at this point.
I don't know if that's what we want to…
where we want to go with this.
I did update this PR to, to namespace those things, so, like, for example, like, for URL, we're just using, reusing the existing url.fool, and for other things, like.
like, for example, refer, like, it's… there's, like, a page in the browser.page.referl, so…
They're now top-level attributes that could be reused in different places, yeah.
**Dan Gomez Blanco** 21:29 Okay, cool.
**Ted Young** 21:32 It's definitely the stuff, the way I think about it, one, entities is, like, super new, so I'm, like, you know, slightly…
about stuffing too much up there. But I definitely think about the… the context you would want. Let's say you have an ex…
You know, some kind of, you know, a fetch request, span…
Or some kind of event, and then you're like, what context is this event happening in? Right? And a lot of that page information, you would always want that context, no matter which span or event or thing you're, like, looking at, you'd want to know, like, what page was this on, whatever. But there's probably a lot of, like, loading and timing and, like, other…
stuff that maybe… You, you… isn't context, so… Yeah.
That's… That's something we should look at. How do we want to break it up?
**Dan Gomez Blanco** 22:23 Cool. I think for now, that's… I mean, as it is, right now, it's good, and then we can make those decisions later.
**Ted Young** 22:30 It's like, what… what… which of these things make good labels for all these other things we're producing?
**Dan Gomez Blanco** 22:36 It can sort of, like, be moved up… moved up a level, right, later, right? If we need to, yeah.
**Ted Young** 22:41 Yeah, yeah, if… if it's… if it looks… and I would say specifically looking at it from the perspective of, like, metrics and things like that, like, which of these things would be good labels?
**Dan Gomez Blanco** 22:52 Coop.
**Martin Kuba** 22:54 So I've taken a lot of time with this, I mean, we're running out of time, so, like, we can continue this discussion in Slack if you need to. I'm gonna remove those two attribute to those two fields, and I'm gonna also, I think, keep the type as a page view type for now, until we model the navigation.
**Joaquín Díaz** 23:13 Muhammad.
**Martin Kuba** 23:14 Okay.
Alright, that's all I have.
**Ted Young** 23:22 I have Google Docs freaking out on me and crashing right now. I'd love some… To crack open some…
Open telemetry on this thing.
Too bad I can't.
**David Luna Bistuer** 23:37 Okay, next is, my topic, which is just, an issue that we… was open before, summer.
Which I think that maybe…
We can close it right now, and the latest JavaScript sync.
I was, mark mentioned that we could have a look and just…
Validate it and see if we can close it right now.
Well, right now not, but just have a look, check is with Lana.
Created a PR, solving some imports.
Anne was asking last month was… this issue was good for closing.
So please have a look, and let's decide to close the door, follow through.
**Ted Young** 24:24 But this… so this issue is just…
Saying, let's look at the logs API and make sure it's gonna work in the browser.
**David Luna Bistuer** 24:33 Yeah, kind of.
**Ted Young** 24:36 Yeah.
I don't know that we need to leave this…
open, unless… are they, like, using this issue to gate, like, declaring the logs API stable or something like that?
**Trent Mick** 24:53 It's not the only thing, but it's one of the things in the milestone for… Okay.
For blessing alongside API, yeah, for stabilizing it.
**Ted Young** 25:03 Okay. Well, then we should, I guess, leave this if the JS SIG is maybe waiting on us to… to do this.
So, someone should… Should take this on.
**Jared Freeze (embrace)** 25:22 I like this one.
Nobody's, interested, I would love to remove node-specific APIs.
Audit, excuse me.
**Ted Young** 25:35 Yeah, you wanna… you wanna audit this thing?
**Jared Freeze (embrace)** 25:37 Sir?
**Ted Young** 25:39 I'm going to add it to…
Well, see, this is… I would assign it to you.
But you're not yet a GitHub org member, so I can't do that.
So, become an org member, let me know, and then I will assign this issue to you.
**Jared Freeze (embrace)** 25:54 Cool.
**Ted Young** 25:59 Okay, 4 minutes left.
Joaquin, you wanted help creating a semantic convention PR?
**Joaquín Díaz** 26:07 Yeah, very quickly, like, I'm working on the page load event.
And I have some draft, like, locally, but I didn't know.
I never created a PR on the same amount of mentions variable, so I… first of all, I didn't know if I had to fork, or I can create a PR directly.
And I didn't know if there is some guidance that I need to follow. But yeah, if you can just link me to whatever I can bid to get started, that doesn't…
**Ted Young** 26:35 Yes, so, I mean, the general pattern is, and I'm sure there's contributing guides in the STEMCOM repo you can look at, but the general pattern.
**Joaquín Díaz** 26:43 There's a speaker.
**Ted Young** 26:43 is, You want to fork the repo, work in your fork, make a pull request from there.
**Joaquín Díaz** 26:51 Okay.
Sounds good.
**Martin Kuba** 26:54 And Joaquin, I was just working on the page… semantic… page view semantic conventions, and…
went through some… just took me some time to understand how to… how to do it right, so, like, if you have some questions, just reach out to me.
**Joaquín Díaz** 27:07 Okay, cool, thanks.
**Ted Young** 27:12 Github repo for browser… I heard y'all talked about this last week. I think we need one.
I've been struggling, I want to make more issues, but I don't want to make all the issues, like, totally clean and perfect right now, and I worry about junking up.
the JS repo.
With her trash.
So, I would like us to make a browser repo for now.
And we can always just… everything we're doing is in alpha state, we could always consolidate it back into the JS repo.
If we decide that's better when we want people to start using it.
I think we'll probably…
be less crazy-making, just because the JS repo's, like, so big and active, if we work in a corner for now.
**Jared Freeze (embrace)** 28:05 Yeah, I like that.
**Ted Young** 28:06 Strong feels. Strong feels really doesn't want us to make a browser repo.
let me know, but otherwise, I'll make a community request. I just need to know who would like to be, and I'll ping people on Slack as well, but who would like to be initial maintainer approver for this repo?
Right, this is not… don't worry about this for, like, any kind of, like, long-term responsibility, right? But…
But for the time being, you know, who, who wants to be…
Paying enough attention to this to be…
Helping me with the backlog and everything else, so… Awesome.
**Joaquín Díaz** 28:43 What is the difference between maintainer and prover?
**Ted Young** 28:48 You know…
In a repo like this, right, where we're mostly just keeping our issues and our design docs.
And maybe, like, some instrumentation packages and stuff like that, I think.
Not a big difference between maintainer and approver.
You get to push more buttons as a maintainer, but I forget exactly which ones they are.
**Daniel Dyla (Dynatrace)** 29:16 There are a couple of important distinctions. Only maintainers, and I think it even says this in the community charter, only maintainers can do releases.
So releases are always gated on maintainers, and at the end of the day, the maintainers are responsible for the quality of everything that is released. So if there is a…
you know, some bug or security issue that's caused by the repo, at the end of the day, that's the responsibility of the maintainers to ensure that that doesn't happen. So, it is…
from a day-to-day perspective, what you're doing, it's all basically the same thing. You're triaging issues, you're approving, you're merging, you're doing all of those things, but at the end of the day, you are the one responsible for the final…
Code quality of the released artifacts.
**Ted Young** 30:15 And in the… to be clear, like, in the long run, based on what kind of work people are putting in, engineering work, we'll see what kind of engineering work different people are putting in to different things, and that will become the basis in the long term for, like, who's maintaining what.
But for the time being, you know, we're just getting started, so I would say use, I want to be a maintainer versus an approver versus just a member as a way of flagging how much time you have.
To help deal with… you know, backlog management, repo, review, blah blah blah. How about that?
**Daniel Dyla (Dynatrace)** 30:52 Yeah, I think there is also in the community charters some… some stipulation for number of hours or days or whatever that you have to dedicate if you want to be a maintainer, so that's essentially that. And then I think maintainers are also expected to have a good overview of everything going on in the repo, where an approver may be focused on just one or two things.
**Ted Young** 31:16 Yeah.
But I would like help, so please, if you're interested, you know.
**Joaquín Díaz** 31:22 Yeah, I think you can contact us in Germany.
**Ted Young** 31:27 Yeah, so write your name down in the notes, I gotta run. I'll also ping people on Slack.
And I'll just let everyone know as I'm making the issue in the community repo and stuff. So, well, there's no need to get this perfect the first time out, but if you're interested, I have to… I do have to seed the repo at least some set of people.
And I gotta run.
I'll see you all on Slack.
