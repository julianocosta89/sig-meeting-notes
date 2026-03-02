SIG: Collector SIG
Date: 2026-01-14
Duration: 17 minutes
Zoom Recording URL: https://zoom.us/rec/share/_hyq396fIZgygBYLmlwLh2LkruEnnPB5JozW0pvvbIBQKh5DtgmRly1dDTGz4GZ_.xAq2k_ozdFN0z7aX
============================================================

## Zoom Recording Transcript

**Perk (Marcin Stożek) | Elastic Ingest** 02:11 Hey guys, how are ya?
**Jade Guiton** 02:16 -Oh.
**Andrzej Stencel** 02:17 Okay.
**Damien Mathieu** 02:18 Hey.
**Perk (Marcin Stożek) | Elastic Ingest** 02:27 Good to see you.
Dabin, I'm hearing you're going to the Ottomplat?
**Damien Mathieu** 02:36 Yes, I am. I… I'm pretty sure I'm not the only one.
**Perk (Marcin Stożek) | Elastic Ingest** 02:42 Very good.
I just booked my journeys as well. So, we'll be there. Maybe Levandre will be there.
**Andrzej Stencel** 02:55 There's a channel, in the CNCF Slack, Hotel Unplugged EU26 or something. Just joined it.
Oh, very good.
**Perk (Marcin Stożek) | Elastic Ingest** 03:04 Have you joined it as well.
**Andrzej Stencel** 03:43 Anybody have anything for the first topic?
**Pablo Baeyens** 03:53 I should have the RFC for semantic conventions ready…
by the end of this week. Sorry for the delay.
I guess I'll share the link.
this one.
And… Well, I'll also share… the stable by default OTAB.
From Austin, just in case somebody wants to…
Review.
Which is… this one.
We're going to bring up the OTEP, like, some… some aspects I want to discuss about the OTEP later with the governance committee on the technical committee.
So, yeah, if you have anything that you think I should bring up, please let me know.
Ideally before the end of this meeting, because the other one is happening in, like, 2 hours.
**Jade Guiton** 05:43 There's a few other issues marked as discussion needed, I don't know if the relevant People are here.
**Pablo Baeyens** 06:03 I mean, the ones about semantic conventions transitioned, I think, ultimately depend on the RFC that I'm putting to my dashboard for review.
**Jade Guiton** 06:11 Yeah.
**Pablo Baeyens** 06:15 And…
I don't know if I have somebody from Prometheus here that can talk about the… The Prometheus ones.
Doesn't look like it's a… Could be… Something we discuss.
In a different meeting.
**Jade Guiton** 06:53 Alright.
This new one, I guess.
Andre, you want to talk about the… PR for renaming components?
**Andrzej Stencel** 07:04 Yeah, it's an issue only, so I created an issue, I took a stab at listing the components that I think should be renamed, if we really want to do that. I was thinking, it's a lot of work, I wonder if we can automate it somehow. And the other thing is, we probably also
when we do these changes, we probably also need to update documentation at opentelemetry.io, right?
Anything else that we should do?
**Pablo Baeyens** 07:34 Update examples, there's some examples, not only on OpenTermacy.io, but maybe on, like, different… repositories.
Across the OpenTool Network.
**Andrzej Stencel** 07:47 Right, the demo, probably. Yeah, yeah, yeah.
**Pablo Baeyens** 07:53 We don't need necessarily to do it ourselves, we could ask the other six to do it, but…
they need to know that they need to do it, I guess.
**Jade Guiton** 08:01 Yeah, and it's not too pressing since we have aliases.
But yeah, I don't know if we need to have separate PRs for every component. There's probably a way to do it as big batches.
So I assume the… I haven't looked… taken a look at the details of the mechanism used for aliases, but I assume it's pretty generic.
**Andrzej Stencel** 08:27 Yeah, I agree, we should probably look at, doing this in batches.
That would be much less worth.
I think that's it. Unless anyone else has anything about this, we can move on to the next topic, Israel.
**Israel Blancas** 08:53 Hi, well, so, last week I asked, people if they can take a look, right, to this
is the case regarding the donation of the EWS.
Justice, sir.
Yeah, well, the only, the only reply that we got right was in…
just a limited ticket, right? Where Tristo suggested splitting it into two different processors. I… if I am not mistaken, I think that when Sean came, presented the processor, there was a similar, conversation, right, and kind of output from the thing, right?
The things that we would like to know if, in case we decide to start Oh…
a Docker attribute processor, right? People will be willing to sponsor it, right? Because otherwise, we are gonna be on the…
Same situation, right? Where… where the thing is not progressing.
very likely, if you are okay with that, I would like to… to get the tickets, right, for… for…
For the new component and everything, but… This is kind of…
a call of attention, right? Just in case you're interested on this thing, right? To get some help about having some sponsorship, right, about this new component.
Nobody has.
anything, right, to say, we can… we can go to the next topic.
Thank you.
**Christos Markou** 10:40 I think we can, yeah, I'm not sure.
I had commented this, we also chatted about this a couple of days, I think, and… Yep.
That's my perspective. I think that would be beneficial for the project in general, to split the logic and have something that is Docker generic processor, since the specific component that you are suggesting already, like, encapsulates this logic.
I think it's better engineering-wise. That's the first part. Then.
If we have the capacity to sponsor
two components instead of one component, that's a different discussion, I think. And, the third also, the third thing here is also that we have changed the, new components guidelines, and we should also take this into account.
My… very…
first answer right now would be that I might… I might be interested into, sponsoring the Docker-specific one, to unblock the work there, because I have done… I've been involved in similar, implementations in the past.
In Elastic-specific, components. And, yeah, but we need to discuss this and see the details. Then the second component, which is AWS-specific, we need to also discuss it.
But first, I'm not sure if we should wait for generic feedback on the issue that you have already, and see what others… what others believe, because that's… right now, that's only my perspective. I'm not sure if we should rely on this or not.
**Israel Blancas** 12:24 Alright, thank you. Yeah,
To be honest, until now, right, it's the only feedback that we got, right? So, it's just, one…
view, right, but it's the view that we currently have. Yeah, so if you are okay sponsoring that thing, I can start working on that, right? And we can start a discussion, also with the… later with the second component.
We'll be happy with that.
**Christos Markou** 12:51 Yeah, I would be fine if some other maintainers also sign in and just
approve the, let's say, the approach to have two different components, if they are fine with this, and if they also… if others also see value into splitting into two different components, and have one for Docker and another one for the AWS-specific enrichment, just to be sure, and then we can take it, deeper
start, discussing the components specifically.
That's, that's my point, more or less.
**Israel Blancas** 13:24 Great. Thank you.
I guess we can go to the next… the next topic.
**Pablo Baeyens** 13:41 Okay, so, yeah, I just have two small announcements. One is, as you may know, there is an, Open Telemetry Focus Un conference called OTL Unplugged.
happening on February 2nd, Brussels,
the day after 4 stem finishes.
If you want to…
attend, or are attending, feel free to join the Slack channel that I put there.
If you want to attend and are having trouble,
getting funding for the ticket, I mean, I think it's, like, 30 euros, it's not super expensive, but,
Feel free to reach out to me or to any other governance committee member, and we may be able to…
Funded to get for you.
And then… the order… thing… Is, we're gonna have a discussion about,
automatically generating JSON schema for component configurations, happening… I… 4PM, CET.
If you want to get the link for the call,
let me, or Evan, or Dimitri know, and we'll add you to the attendees list. In any case, we will, of course.
Post anything on… on GitHub, but yeah, just… we wanted to coordinate since there's several people that are
Interested in this.
**Evan Bradley** 15:30 I also have an item on here.
We're planning to do some changes, driven by Bogdan to,
make pretty substantial changes to OTL's API. The goal is that we're going to try to add some additional type safety. But as part of this, instead of doing a, a gradual shift, the plan is just to do some, just a clean break, the goal being that
We can do this before OTTL, goes stable.
But I just wanted to, let this crowd know that, if you have any concerns about this because you heavily use the API, or if you just like programming languages and, have some input to offer, we would appreciate, your participation.
**Jade Guiton** 16:18 Is this about making the internal API type safe, or about making the… The language itself typesafe.
**Evan Bradley** 16:27 So, it's about… it's a little bit of both. So it's about making the language itself type-safe, but in order to do that, we need to change how all of the getters work, so basically the interface between… So to add type safety, we need to change the interface between OTDL's functions and the underlying P data that they work on.
And as a result of that, need to make
Pretty substantial breaking changes from the, function author standpoint.
**Jade Guiton** 16:56 I see.
Any other impromptu points?
If not, I guess that's it. Thank you, everyone.
**Evan Bradley** 17:32 See, everyone.
**Damien Mathieu** 17:33 Thank you.
**Pablo Baeyens** 17:34 Thank you.
**Andrzej Stencel** 17:35 Thanks.
**Perk (Marcin Stożek) | Elastic Ingest** 17:37 Thanks, Gerald.
