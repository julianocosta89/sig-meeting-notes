SIG: Semantic Convention SIG
Date: 2026-02-02
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/RfVLaRV0bku1ox0m8tKSkx2t2QjlyWmMwm1q1etrNTVoLd0FTUoImwLJaAs1uZ0x.AfZYuBg8k0V8oZX0
============================================================

## Zoom Recording Transcript

Josh Suereth 00:04:07 can I… is my speaker broken? I can't hear anyone. Do I need to re…
neil yashinsky 00:04:13 I think people are… I can hear you.
Christophe Kamphaus 00:04:15 one.
Sven Cowart 00:04:15 There you go.
neil yashinsky 00:04:17 I wondered the exact same several times.
Josh Suereth 00:04:21 Yeah, I saw Trask talking. Oh, my camera's not working either, let me fix that, but my camera's broken. Trask, I think your mic wasn't working.
Yeah, now we can hear you.
Trask Stalnaker 00:04:30 Ayyy, that's useful.
So I was just going through triage, apparently, with myself.
neil yashinsky 00:04:45 Happens to the best.
Trask Stalnaker 00:04:48 Adding, okay, this… So we…
do have the required approvals, so I guess the… Oh, just recently, alright.
Ha.
Awesome, so we can move this to… Ready to be merged…
This has acquired approvals, also, as of today.
Actually, let's just so… I will move that also.
Make criticality… okay, this one… I think there was some discussion… .
Josh Suereth 00:05:50 Yeah, I can speak to this, but basically, we're in a weird state right now. This is,
So, service, the entity, has an exception for policy around stability.
Mostly because, like, service, the entity, doesn't actually exist in instrumentation, people just fill out environment variables.
And so… we have a thing where we're starting to apply, like, rules in our model around stabilizing entities, and, like, what that means, and how if you have a stable entity, all of the attributes should be stable, or they have to be opt-in, that sort of thing. How that interacts with description.
Basically, the default group behavior for attributes was triggering on entity, and so part one is, I don't know if that should happen, and I think we need a discussion about what the behavior should be around stabilizing entities and descriptive attributes, and how we want that to be moving forward. Second,
We… we can't mark it not stable.
The… at least the attributes service name is already stabilized and used everywhere in hotel. And then third, we're adding things to service, so we need to figure out what that means. Like, what… what policy do we need in place to safely
Add non-stable things to service.
and then mark them stable later, and have them be the way we want them to be. So I think…
for this PR, what I'd like to do, if we want to label, service criticality as opt-in, that's fine. Technically, that's how it is today, because any service attribute, you have to fill out manually by using an environment variable.
So it's not like any of these things are automatic out of the box to begin with, so that's fine for me now. But…
I think the discussion around this… I still think service should probably have an exception around stability, because I'm not positive that we have stabilized the entity. I think we've only stabilized…
the name.
If that makes sense. And the second thing would be, I think we need a discussion, and I can take this to the entity SIG, which is right after this, of what are the stability rules around semantic convention definitions we want for entities.
And what kind of evolution do we think we have in place for, once something's marked stable, what are changes you can make to that stable thing that are acceptable? And then we can update our policy. But the TLDR is, the policy we put in place for spans and metrics just implicitly happens
on entities. It's not clear if they should be exactly the same or nuanced, because entity attributes have subtle differences. There's an identity and a description, and identity is required, and you should not be able to ever add anything to it, and so we have rules about that that are custom.
To entity, and not anything else.
Do we also need to do that for descriptive attributes for entity? That's, like, question number one.
Second would be… yeah, go ahead.
Trask Stalnaker 00:08:57 I'm… So, for… you mentioned it was inherited from…
spans? Because, like, I understand, I mean, if it was inherited from metrics, we have these rules, but for spans.
I assumed that we could add non-required
attributes to spans, so I assumed we could add recommended attributes to spans.
Josh Suereth 00:09:23 The current policy is you can only add opt-in.
To a… like, if the attribute is not stable yet, It can only be opt-in.
Trask Stalnaker 00:09:36 Okay, that…
Josh Suereth 00:09:37 I wonder if that.
Trask Stalnaker 00:09:38 necessary.
Aye.
Josh Suereth 00:09:40 I'm okay with that. What I think needed to have… like, what I wanted to have a discussion about on this was not just to blindly do it, but to actually have some principles around, like, what entities should look like going forward, right? That's kind of why I was like, look.
There's literally no instrumentation that this decision will break right now. At all. So we can do whatever the hell we want.
But let's, let's figure it out now, before we just blindly do this.
neil yashinsky 00:10:09 Halfway forward. I like it. That makes sense to me.
As the newest person here.
Trask Stalnaker 00:10:19 I'm… Josh, sir, if you say the entity… you're gonna take this to the entity SIG,
Say you come back with that, you know, descriptive attributes can be
Recommended. Can be added as recommended.
Then we still need to have that discussion for spans.
Because I really did think that… I don't personally see a problem with adding Recommended attributes to spans.
I'm not… I'm surprised that we have a policy against that.
Josh Suereth 00:10:56 Well, so, you know the stable by default policy that's getting rolled out, that OTEP?
Trask Stalnaker 00:11:01 Yeah.
Josh Suereth 00:11:02 I think that what we're going to have to do is, if there's a stable signal anywhere.
And there is an unstable Attribute defined on that stable signal.
Right? Like, we're evolving it, we're adding something to it and trying it out. We need a period where that happens.
There should probably be a feature flag definition somewhere.
So, like, I would be fine if we said, cool.
I think implicitly, it's always opted, because of the stable by default thing.
Trask Stalnaker 00:11:35 Yeah Right? So implicitly, it'll be opt-in.
Josh Suereth 00:11:38 But I think what we want somehow is to say, this should be recommended when it stabilizes.
Trask Stalnaker 00:11:44 Yeah.
Josh Suereth 00:11:45 But here's the feature flag that you use to opt-in while it's unstable. And I think we need to… like, that's what I would like to make happen here going forward for this. It's just, all these things, you know, what is it? It's a conflagration of, like, 5 different things going on at the same time, and… yeah.
Trask Stalnaker 00:12:06 Okay.
Josh Suereth 00:12:06 So, if we wanted to merge this PR as is, again, I actually don't think there's any problem merging it or not merging it.
Because…
again, we don't have instrumentation that makes service criticality. Users will engage with it opt-in all the time now, today. That's how the demos around service criticality worked to begin with, was it was just, you know, they provided it on the environment variable. So, if we marked an opt-in, doesn't bother me.
What, what I… what we need is the,
we need the next step, where it's, okay, what's the path forward here? What should this look like? What do we do as stable by default? Let's get our policies sorted out. So, I think that that should probably be tracked in an issue, maybe? What do you think, Trask?
Like, I don't want to just block this PR indefinitely and solve it in this. I want to actually have a task to do so.
Trask Stalnaker 00:13:00 Is this,
Do we need to get this in? I mean, is there any urgency in getting this in?
Like, it's breaking some… like, our policies are broken today.
Josh Suereth 00:13:12 No, our poli… we have… right now, service has an exclusion, so it's possible that you could add something to the service entity that would violate policy in the future.
I… again, I don't see that happening, because the service and deployment SIG is doing the reviews, and…
Yeah, so… go ahead, Jan.
Joao G. (Dynatrace) 00:13:30 Yeah, so I just wanted to say that the other option is just not do anything until we decide, like, now that we, like, if we decide with the entity SIG and we have a proper plan, then we can just do it.
Because if we get this in, then we have… I think we are in even worse, because then we are in a very mixed state. Some things marked opt-in, but the rest is not.
So I also, like what Josh, proposed, so we just… I'll just not merge this, maybe just skip it, and then, we have the,
Exception for the service thing, and once we figure it out, then we come back.
we come back to it and do it. It's not causing any harm anyway, so I think it's…
I think it's fine.
It was good to find this out now, but yeah.
Trask Stalnaker 00:14:21 Sound good?
neil yashinsky 00:14:26 Gosh, and I just added your, like, the quote, sorry, this Adam, to your agenda, but I didn't catch your questions in time, so if you want to just reflect the questions that you had in the agenda…
Trask Stalnaker 00:14:40 Alright, I think we are out of our triage time.
Joao G. (Dynatrace) 00:14:45 I just moved it to, block, by the way, just FYI.
Trask Stalnaker 00:14:49 Okay.
Perfect.
So let's hit the agenda.
Okay, let's see. So we've got 20, 25, 35, 45… Okay,
I think this one can probably go a little…
shorter, and so we don't have Lyudmila here today.
But I did want to, get sort of a broader…
view of this proposal. We've been discussing it… we discussed… we've been discussing it in the LogSig.
But it's a… fairly, I think, fairly significant, proposal, so I want to make sure that
We're kinda… there's… Broader community support for it.
The idea is that,
So, with events, we have… we have already recommended that events use the attributes.
To model their data, as opposed to the body, and that is…
Well, we've always had complex attributes on the log signal anyways.
One thing that has come up… So, is,
sort of what to do with the body. Some people have wanted this convergence of events with sort of classic logs, like if you're…
Dreaming them all together, and your classic logs have log bodies, strings, and your events have these structured attributes.
You know, what…
Do you display, sort of, in some cases, it could be nice to have, like, a display message.
You're, in the event body.
So it would be things that are…
Basically, just summarizing what's in the event.
attributes already.
neil yashinsky 00:17:17 And is this as a means of providing, like, just a separate alternate, you know, option, since people have… to enable choice, essentially?
Trask Stalnaker 00:17:29 Yeah, it wouldn't be, like, the… the real data of the events would be in the attributes. This would just be a sort of…
Summary or display message.
And it wouldn't be required for all… Events… so,
I think there's some… yeah, might be missing some context here.
neil yashinsky 00:18:10 But it…
Trask Stalnaker 00:18:11 Yeah.
neil yashinsky 00:18:12 Can I just ask one last question to the… and forgive me if this is new, and I'll be quiet if I can, but it seems like there's some, the… is there… what's the second closest attribute, I guess, today to, like, display message that's the alternative for people to use if they didn't want to use,
it, and they wanted to use display messages. Is there something that's just, you know, naturally similar, or is it just… there's nothing really comparable?
Trask Stalnaker 00:18:36 There isn't, and we had discussed…
That having an attribute for that, that is an option, like, an event.summary attribute could be used.
neil yashinsky 00:19:02 since nobody has any strong opinions, seemingly, I'll just, I'll just,
Offer one last point, which is that it seems to me that some amount of…
I guess I'd call it, for lack of a better word, like an analysis attribute, a summary attribute,
you know, absent something that is canonically, like, what this is all about, this message, it sounds like…
Some kind of, like, the user-facing aspect of this is… is… Necessary and, and needed, even.
I think this one… oh, sorry, go ahead, Josh, please, or someone else.
Trask Stalnaker 00:19:55 There was also… previously, we had some discussions about,
Like, the body being a good place for, large… data, so, like, HTTP events…
we had thought that the body could be a good place to put the HTTP request or response if you were, you know, doing
Debug level.
Stuff.
So I guess we're kind of, and it's… it's come about because we're trying to,
stabilize, sort of, some of these documents around events here, so this one's still in development.
So we're trying to make recommendations for what to do with body.
And these are a couple things that have come up.
neil yashinsky 00:21:07 Yeah, I just figured, kind of, like, in,
based on the historical nature of formats, and I think sometimes we're using that word politely, right, because some of these log messages have, like, very…
loosely defined patterns, if at all, that we have to support, or whatever, ensure…
you know, is… we can match or whatnot, and I think, like.
There's gonna be a lot of…
I guess I'd say variation in how people adopt this in particular versus, I think, others, where there's just less of a historical…
I don't know what you want to call it, technical debt associated with the, you know, with the evolution of these things in kind of on their own, versus, you know, something like Traces that I think had a little bit more stability, maybe just because of the nature of what it was or whatnot.
But logs are always been kind of a… a wild, wild west, if you will, of output.
Trask Stalnaker 00:22:13 Yeah, I think that's the thing that I most like about this proposal, is that it does sort of dovetail into,
Non-event logs, sort of your existing logs.
neil yashinsky 00:22:33 Traditional logging structure? yeah, agreed.
Trask Stalnaker 00:22:40 I don't know if we want to go further and say that that is the purpose of the body, and sort of,
Scope out this idea of using body for large data.
I mean, we can put large data in attributes.
I think there was some thought that maybe some backends preferred it to be in this body field, like, that would be some signal that that could be a large thing.
Josh Suereth 00:23:19 Yeah, I…
I'll say my current thinking here, and this is just bringing it up a level, is I think there's,
the problem with logging in my mind, there's OTLP,
And then there's how everyone else does logging today.
And I think fundamentally, if we can't support someone dumping a big JSON object
On one line, and reading it, and turning it into a log.
Then our login model has problems.
And if we can't write in that fashion, because there's so much of the industry that does that.
So, I… I… you know, when it comes to, like, body versus attributes versus… I…
you know, whatever. That's part of the problem. But there's, like, a few use, like, things that people do today, systems in place that I think we need to interact with, and that's where I think the interesting
questions get answered with this, right? Of, like, what does this look like with a system that just accepts JSON and takes JSON? What does this look like if we're accepting in raw JSON and trying to feed it into OTLB?
You know, The… What does it look like with raw strings? You know, in the logging industry.
There's a thousand different formats, and so a lot of these, you know,
There's the syslog D, which has a known format, but kind of doesn't, you know, you still have to parse the hell out of it.
You have these, like, stringy formats that you parse out, but it's still, like, align stuff.
To the extent that we can support that with what we're doing, to me, that's the important bit.
to the extent that those common conventions and things have places to go, that's the important bit.
I know that we're trying to unify between logs and spans, so that you use attributes for both, that's great, but then, you know, all of this should just be grounded on what large-scale logging systems do today, you know? Like, what someone who sets up an old elk stack, what do they look like going forward?
someone who's using SyslogD, what does that look like? That's… that's what I want to ground all these things in. And I don't know if any of the conversations I've heard around this so far ask those questions. They all focus on what OTEL does. Cool.
I agree that that's important, but I do want to just ground it on, like, you know, real-life logging.
In terms of how I would change that, anything you're doing here, by the way,
If body happened to just be a string, I think we'd be fine.
Like, we could go that far.
Trask Stalnaker 00:26:13 Yeah, I think there… so, the Leipzig is…
Pretty much… mostly just focused on events, And… Exceptions, currently.
Exceptions may… There's kind of an open question. I think we may model some exceptions as events, give them event names, like, things that kind of… to kind of connect them to their spans.
Like, http.server.exception.
But miscellaneous exceptions might not have an event name and might be… Fall under that.
Classic log.
But that helps.
I think I'll kind of push a little bit more on the… Body being the stringy thing.
Since that is… does align With classic logging.
more.
Alright, let's, we've got… Let's move on. This one…
So, starting to push forward with peer.service renamed to now a service.peer.name, so it's starting to apply this to the Java instrumentation as an opt-in, so that we can adapt, we can take that, breaking change into our next major version.
So you'll see I have a PR to stabilize them, but I realized that service namespace, needs to be stabilized first, so there is another PR to stabilize that, so that's good.
I think the… Reason I wanted to bring this to this group was…
Any thoughts on… so, as far as modeling this in the config YAML,
So we've got this general, instrumentation general place where we're putting these kinds of things.
Does it feel like service, and then peer mapping?
fits this. Like, it's underserviced things.
Or do… like, my only hesitation was that service is kind… generally things that apply to the local service.
And so that could be confusing.
I mean, I could do service underscore peer, here, and then mapping…
Josh Suereth 00:29:24 This is where I usually have bad naming suggestions, so I'll just say that I…
what I'm looking at looks fine to me, the two that you're proposing. I don't… yeah.
Trask Stalnaker 00:29:35 Okay.
Cool, then we don't need to spend, more time, let's see…
Alright, let's go to Serbi.
Surbhi Agarwal 00:30:08 Hello, everyone.
Let me share my screen.
Trask Stalnaker 00:30:13 Sure.
Surbhi Agarwal 00:30:20 Can you see my screen now?
Trask Stalnaker 00:30:22 Yeah.
Surbhi Agarwal 00:30:24 So this was regarding… Adding the network timing for the different network phases for client instrumentations.
We did have quite a bit of discussion, in the semantic convention sig as well. This is an issue in the semantic convention repo.
I was asked to create a prototype of the final suggestion that we finally landed to.
So, basically, to give an overview, this is something similar to the browser resource timing, event.
Which is sort of… contains the timing for the different phases that happened during a network or a resource fetch for a browser.
So there are, PRs for… from the browser folks to add something similar. Basically…
Something of this sort, wherein it is a standalone log record.
That contains the various timing that are needed. So, the backend would use these two timestamps to calculate the connection duration and generate charts out of those.
For, like, metrics, gathering purposes. Similarly, for client, I created this PR for the OKHTTP3 client, in the Java instrumentation repo.
Where, I, implemented something similar, storing these timestamps. So, I wanted to, get the…
feedback from this SIG, get it approved, create a generic sort of unified semantic convention for both mobile and browser, and then go forward with my PR being merged, for the instrumentation as well.
So, the proposal is to have a standalone log record.
With the name something like HTTP Client Network Timing.
the context would contain the context of the original HTTP span with all the data, so these can be tied in together at the backend. The attributes that would go in this would be…
the call start time, DNS, DNS end, connect start, connect end, secure connect start, if it is a TLS connection.
The header start, header end, body start, body, end, for both the request and the response.
Browser might not have all these, so for browser, there is just a response, there is no headers and body separately, so they would use this for the start. They don't have a response end. Their response end is, like, the end of the fetch, so they would use call end.
And then these are a few things that are there for browsers specifically. So, I added these.
So I mentioned that browser might not have the granular phases, so they can use,
Like, the top-level ones, and they have some extra ones.
Then, right now, backends sort of generate
metrics at ingestion time. They do not have the capability to correlate to different
signals to generate metrics, right? We need to tie together the original HTTP span and this timing log to be able to generate the full metric, data, right? So, like, in the interim.
to support backends, we would be copying certain HTTP span attributes in this log record as well. Some of these important attributes would be
the URL, the request method, the status code, server address, server port, network-related stuff, which is important for the connection metrics, then the exception type, and the payload size becomes important as well, of the request and the response.
So, this was, the suggestion, so I wanted to, get the feedback of the SIG on this.
RC Robert Cowart 00:35:02 I had one question, but I can't find the hand-raise thing, so I don't want to be rude if someone was… You're good, you're good. Okay. My question is,
basically… if this is trying to capture, in general, all HTTP-based requests, should it also include quick.
Or is that viewed to be here as something entirely different?
Surbhi Agarwal 00:35:29 I'm not aware of Quick, is that an HTTP client?
RC Robert Cowart 00:35:34 It's basically, I mean, our gentleman from Google here should be able to tell us way more about it, because they're the one that made it. So, the… but, it's essentially…
does not use TCP. I actually think all of your fields probably fit your definition of connect start time and end time, though, specifically calls out TCP, and quick is UDP-based. But you still have TLS and other attributes there, so if you're purely thinking of this as a Layer 7 record.
then I would argue that quick…
It's covered under this as well, but maybe a couple definitions need to be tweaked.
Surbhi Agarwal 00:36:11 Got it.
Yeah, I would, like, love to make it as generic as possible, so it fits the…
Semantic con… it justifies being a general unified semantic convention, right?
Josh Suereth 00:36:27 Yeah, so…
I wanted to jump in for a different reason, but yeah, I think supporting Quick would be awesome, and just because I work at Google doesn't mean I know Quick. I'm not on… anyway.
You know quick, I just wanted to… anyway, so, yeah, quick…
Quick support would be great here. The thing I'm looking at, though, is what I'm seeing is what looks kind of like…
A bunch of metrics, or what we would call multivariant metrics, and you're putting these into a,
You're putting these all into an event, right?
This is where you're gonna have something that kind of tracks individual span-like things and reports them all in one big bundle? Is that correct?
Oh…
Surbhi Agarwal 00:37:12 I would argue not span-like things, because we just have the timing data here, and not…
It is not a detailed DNS instrumentation, wherein I also need the timing and the attributes related to the DNS step, right? That would be a span. But here, I just need the various
events and time, so I capture various events in a log record, I would say.
Josh Suereth 00:37:41 Right, but okay, so are these individual log records, or do you have one log record that has all of them?
Surbhi Agarwal 00:37:47 One log record for all of these.
Josh Suereth 00:37:51 And… Yeah. Go ahead.
Surbhi Agarwal 00:37:53 The rationale was, like, it would be too much, right, to emit so many events, and then the backend having to tie so much. It is related to one HTTP request, so why not put them all together in one log record?
Josh Suereth 00:38:06 Yeah, like, what I think is going on here, if I were to think about this from how I'd instrument it, right? Your DNS, you're recording the start time and the end time, which is equivalent to having, like, span instrumentation.
I was saying start spin, end spin.
like, there's… there's not a huge difference in what I, like, your code looks like and what… what this looks like.
Why I want… I want to hold off on making a semantic convention for this, and I'll tell you why. I don't think OpenTelemetry is giving you good support for what you want to do. And I don't want to hijack how OpenTelemetry works to fit what you're doing.
I would like to actually explore whether we can do better with the browser SIG,
And then define…
a convention from there. So what we're trying to do, by the way, is you should be able to have this event defined somewhere that you keep stable and advertise to people, but it's not part of SEMCOM, it's part of your instrumentation.
And we can still share it, we can still explore it with people. But I think OpenTelemetry can do better for you here.
And I don't want to block what you're doing, based on that. But I also don't… like, when I think of how you would write the code for this in the browser, it looks to me like it would be a bunch of spans.
Where I would have, you know, start, stop tracking, start, stop tracking for all these things. Then I would collect all those spans for that request into, like, one thing, and then generate an event that fires out, right?
That… that seems to me like what's happening here, and so I feel like there's something missing in OTEL.
to keep this efficient for the browser SIG that is leading to
this, right? Of the proposal. Like, what you're doing makes a hell of a lot of sense. Like, let's optimize this, let's get this whole… all the information about a request down at once,
But it… it might… in the back of my head, this just is telling me that there's something missing
in OTEL for browser that's causing this design, and I don't know if I want to lock to this design without fixing that underlying thing. Like, I'd like to…
let people do this for now, and explore that, and then also try to solve the underlying problem. Anyway, a bunch of hands, I think, from BrowserSig. Go ahead, go ahead. I think Daniel was first, and then Christoph.
Daniel Dyla (Dynatrace) 00:40:28 Yeah, I was first. I think, I just want to clear up what's possibly a misconception here. As far as I'm aware, this comes from the resource timing API. You wouldn't be…
tracking start and stop with, like, the span API, you make a call to the resource timing API, it comes back as an object.
And it has all the timings in it already. So, like, creating a bunch of spans would then be a more inefficient solution than just emitting what is essentially already provided by the browser.
Josh Suereth 00:41:01 I gotcha, so this is just… so from my understanding, this is just taking resource timings and dumping it as an event. Like, I just call that, get the data, dump it out.
Daniel Dyla (Dynatrace) 00:41:09 I'm not an expert on what exactly comes back from the resource timing event, and I haven't read through this PR in detail, but that's the way that I understand it, yes.
Surbhi Agarwal 00:41:18 Yeah, there's something similar, for, yeah, we are not creating different spans, like, for OKHTTP library, for client as well. We have a…
Event Listener, which has all these different callbacks.
So we just define an event listener and patch together all the different, timing that we receive from all the different, callbacks.
That… what you mentioned, Josh, definitely makes sense. What earlier made sense was to have these as separate span events.
But, that is not possible, because pan events, there is… there are plans to deprecate those.
In favor of standalone events or logs, right? That's why the suggestion… it would have made… in OpenTelemetry, if you think about it, it would have made sense to have these as events in the actual HTTP span.
Josh Suereth 00:42:30 Yeah, you, you can still have multiple events, by the way. Even… so, so, like.
The… a log actually has a reference to the span that it's a part of, as opposed to being nested.
So you don't get the nesting benefit, but anyway, I… the… okay, I'm gonna… I'm gonna stop, because I think I understand what you're doing now better, and I'm not… like, what I said still applies, because I still think OpenTelemetry can do better for you here. This… this still feels like multivariate metrics, or some sort of, like, multiple measurement thing going on that OpenTelemetry's bad at.
That you're working around. But I think what you're doing is, like, technologically totally fine. It's just, there's a piece… I want to dive in more to figure out what OpenTelemetry could do better here.
And if I'm understanding this correctly, I can send…
There's a lot of these that are opt-in, so I don't have to send all of them, right?
Surbhi Agarwal 00:43:27 Yeah, correct.
Josh Suereth 00:43:29 Cool.
Alright, sorry, go ahead, Christoph, I didn't mean to…
Christophe Kamphaus 00:43:32 Yes, that directly ties into what I'm thinking about. What happens if You have an arrow.
For example, you resolve DNS, so you would have the timing for that, but then you failed to connect.
which will then only report DNS, which you report Connect.
Surbhi Agarwal 00:43:50 Yes.
Christophe Kamphaus 00:43:51 Yeah.
Surbhi Agarwal 00:43:51 So, the idea is to report whatever you are able to fetch.
Christophe Kamphaus 00:43:57 Yup.
Surbhi Agarwal 00:43:58 Yeah, and, like, for instrumentations, like, going… yeah, the idea is that if, like, call end time would be probably there every time, so whenever it ends, you, like, have this call start and call end.
Christophe Kamphaus 00:44:17 Okay, but if no redirection happened, for example, you wouldn't report that.
Surbhi Agarwal 00:44:22 Correct.
Christophe Kamphaus 00:44:24 Yep.
Surbhi Agarwal 00:44:31 That's why these sort of, like, are also not required, because there are connection pooling, right? So these might not be there always, so these are recommended, not required. This is the required ones only.
Trask Stalnaker 00:44:49 My two pieces of feedback, one is the, the start time, end time, all of those timings.
It looks like you're defining those as epoch?
Times… Yeah.
If you look at the browser resource timing event proposal, I think those are…
Timing since the start.
As opposed to full epoch times.
Surbhi Agarwal 00:45:29 Yo.
I was, that was a question I wanted to bring up as well.
My rationale behind using an epoch time in the proposal, is so that we also have the actual time
For this particular thing, for backends which want to show, let's say, a timeline.
And also, we have the different times for them to subtract and calculate the duration. With this.
Just having… From the origin, the time for these different events.
Then we won't have the exact…
time stamp. I'm not sure how important that is.
Trask Stalnaker 00:46:13 Why, why won't it be the exact timestamp? Why can't… why wouldn't you just add the diff on top of the start time to get the timestamp?
Surbhi Agarwal 00:46:26 Okay, got it.
we can get them. But, like, a follow-up question, why are we preferring a diff rather than an epoch time? Is it, like, smaller data?
Less data.
Trask Stalnaker 00:46:41 The big thing for me, at least, is that, it allows you to use a, monotonic timer on the OS, like, to get,
the… those deltas?
As opposed to epoch times, which are not guaranteed to be monotonic. People can, you know, the clock can reset, the leap seconds, things like that, it's just generally preferred to use
In Java, it's called nanotime. It's just… for, specifically for doing, deltas.
Surbhi Agarwal 00:47:28 Got it.
Daniel Dyla (Dynatrace) 00:47:29 It's also not as trivial to convert those performance times to real times as you would expect, because the performance
Timers, sometimes pauses?
In some situations, we have had several…
bug reports in the past in the JS… Sig… From, you know.
from assumptions around the performance timer. Like, one example is that Chrome will pause the performance timer if the tab is in the background for too long.
I don't think it's likely to affect anything in the space of a single HTTP transaction like this, but the… the performance timer is shared… is used… is for the entire page, so if your page pauses for any significant period of time, and then you make another request.
Any, like, conversions from that to real time.
Are potentially incorrect.
So… yeah, it's not as trivial as you would expect. My recommendation would be to…
Save and transmit
The data that we get from the browser with a minimal processing, and a current timestamp.
So that the backend can treat it however it deems appropriate.
Trask Stalnaker 00:49:01 So, just to clarify for everyone here, there's kind of two different, but somewhat similar
topics here. One is the browser resource timing event, and this one is, more targeted at mobile, like, OKHCP is kind of the initial target.
So not browser.
But I do, think they're very, like, it's good to align the… the semantic conventions where possible.
Christophe Kamphaus 00:49:40 I think another thing is, if you have relative Times.
Your analysis backend can do statistics more easily on those.
Trask Stalnaker 00:49:58 My other… my only… my other feedback, Serbi, is the,
Copying attributes from span down to event.
Which I think I like. Like, initially at my, like, like, we…
as Josh mentioned, the event is tied to the span, so backends can do that correlation.
But we've been having this same discussion around exceptions.
Of, like, so if a span, if an exception, bubbles up, causes a span to fail, and we emit that exception as an event.
There might be, like, there might be some benefit there to stamping some of the span attributes onto that.
For, the use case you described, which is, log telemetrics, event to metrics, pipelines.
That then don't need, you know, can do that in the collector, as opposed to having to do it in the backend, where you have to wait for both the span and the,
The event to be co-located together.
Surbhi Agarwal 00:51:18 Hmm?
Yeah.
Earlier, I did plan for… Maybe having a configurable setting so they can choose what they want to include?
Or maybe copying everything, but then these sort of seem like a good middle ground.
Set of important things that they might need for the metrics that they can drive out of these.
Trask Stalnaker 00:51:46 But I am curious if anyone has thoughts, because I think it's a…
Sorta. We have generally tried not to duplicate data?
Then… and say, hey, you know, we're already correlating everything together.
Why duplicate? So, we haven't decided anything in the, log sig around exceptions, except that that topic has come up.
Surbhi Agarwal 00:52:15 Just wanted to add, like, for this, it would be a configurable Boolean if they wanted this. So if they don't want this, and they have something already at the backend to do it, they can set it to false, and these won't be added.
Trask Stalnaker 00:52:29 I see, so these would all be opt-in?
Surbhi Agarwal 00:52:32 opt-in, yeah.
Trask Stalnaker 00:52:37 Okay.
Right now, they're mentioned as, like, required and recommended.
Surbhi Agarwal 00:52:44 Yeah, I will correct that. Maybe URL is required, like, from the browser use case, if I see, they have proposed this and this to be required.
Others are sort of, yeah, opt-in.
Trask Stalnaker 00:53:05 Yeah, I'm not sure on the browser side if they are connect… if they have a overarching span. I think they're not even capturing a span.
But I'm not sure.
And only doing events, possibly.
Surbhi Agarwal 00:53:22 I think they do capture span, but I'm also not too sure.
Was there any other feedback on this part?
Okay, hopefully this looks good.
For this one, like.
What would be the, like, to… going back to our earlier discussion, right, we mentioned that probably deltas help, but browser use case might not.
work well with that. But then also if, suppose we were to use deltas, right, the start time would be something…
it would have to be something of a, like, a timestamp, right? It can't be delta, and then everything else is a delta to that.
Trask Stalnaker 00:54:16 Right.
Surbhi Agarwal 00:54:18 Okay.
Got it.
Trask Stalnaker 00:54:20 I don't know if it makes sense for that to be the event time itself.
Surbhi Agarwal 00:54:28 Yo.
Okay. I think that is something that needs more work on.
That'd be cool.
Christophe Kamphaus 00:54:36 What's the time you emit the event.
It would need to be after it, because all the… requests… It will have finished already.
Is that what you meant, Rusk?
Trask Stalnaker 00:54:52 Yeah, yeah, it's not… I'm not… I had… would have to look at what the event…
Time is supposed to be, like, if it's op…
Supposed to be the time that you omitted it, or if it can be, like, backdated.
Surbhi Agarwal 00:55:11 The time that the log record is emitted is…
not useful, sort of, in this scenario, but…
It is emitted when we are able to… like, when the call is founded, and we received all the data that we wanted to receive, right? These timestamps are important.
And, like, for OKHTTP3, this is the exact time when the request started. Like, I… we have event callbacks, and I'm guessing for browser use case also, you get that object back that contains the exact time when these things happened.
I'm not sure of the browser use case, yeah.
Trask Stalnaker 00:56:02 Alright, yeah, I mean, there's… it's a…
complicated topic, but I think we made some… Progress, hopefully.
Today, Servi.
Surbhi Agarwal 00:56:14 Yeah.
Trask Stalnaker 00:56:15 You're welcome to stop by the LogSig tomorrow. We might have some time to sort of discuss event modeling options there.
Surbhi Agarwal 00:56:28 Sure.
Yeah, that sounds like a great idea. So, like, in the interim, so, like, we are holding this off as a semantic convention, we are going to refine it more,
And also, like, see if OTEL has… can improve to provide us a better signal for this kind of a thing. And, like, is it okay if we go forward with figuring out the…
minor, things that were open for these PRs, like, for the OKHTTP3 instrumentation, like, we need to figure out this thing. Otherwise, we do have sort of a consensus on where we are headed, right?
Trask Stalnaker 00:57:09 I think you'll just need to keep iterating.
And we'll keep… you know, getting feedback, I…
Surbhi Agarwal 00:57:20 Yeah.
Trask Stalnaker 00:57:21 This has been a very… Daniel will attest that, client-side events is…
Tricky and has been an open topic for, like, 3 years now.
So I wouldn't expect to have a decision, you know, final decision in a week here, but I think you're making good progress.
And, happy to continue iterating.
Both here and in the Java repo.
Surbhi Agarwal 00:57:52 Yo.
like…
until we have… which would take time, right? Until we have a proper plan, semantics around it, like, would it be fine if we went forward with this…
And we can correct it as needed later on. This is something that we plan to… we use these instrumentations in our repo, and we plan to have this soon. So, was wondering if it is possible to get this merged, and then based on what we decide, we can change it as needed.
Trask Stalnaker 00:58:28 So that's a question for the JavaSig.
Surbhi Agarwal 00:58:31 Yo.
Okay, let me bring it up there again this Thursday.
Trask Stalnaker 00:58:40 Sounds good.
Surbhi Agarwal 00:58:41 Thank you so much. I'll reiterate on, the other semantic convention issues as well.
Daniel Dyla (Dynatrace) 00:58:52 I'll forward this to the browser SIG folks, but I'm actually gonna be…
gone, so I won't be at that meeting. I can't… normally, I would say I would bring it to that meeting, but I can't this week.
Trask Stalnaker 00:59:06 Yeah, but even next week,
Serbi, you know, getting alignment with the client,
the browser would be a big step towards getting confidence from other people, including the Java maintainers, to,
Go forward with the prototype.
Surbhi Agarwal 00:59:29 Definitely, yeah. I'll try to bring it up everywhere, and… Yeah, see where it goes.
Trask Stalnaker 00:59:40 Great. Sorry folks, we have run out of time. I know we had…
A few good topics lined up still.
So we can try to follow up on those in Slack.
And… Next week.
See y'all.
RC Robert Cowart 01:00:06 Thanks, Tim.
Surbhi Agarwal 01:00:07 Thank you.
Christophe Kamphaus 01:00:08 See you all.
Armin (Dynatrace) 01:00:09 Bye-bye.
neil yashinsky 01:00:11 Thanks, bye.
