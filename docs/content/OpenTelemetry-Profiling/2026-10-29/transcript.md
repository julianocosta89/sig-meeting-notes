SIG: OpenTelemetry Profiling
Date: 2026-10-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Felix Geisendörfer (Datadog, Inc)** 07:29 Alright… Hello, everybody, and welcome to the hotel Profiling SIC.
As usual, we'll start by going through the review of previous action items.
I see that we have currently no agenda items beyond that, so if anybody's here who wants to ask a question or propose a topic, please put it on the agenda, so we'll cover it once we get to the action items.
And then, I guess, without further ado, we can go through the action items. Unfortunately, the updates on my end are that I didn't have time to work on things. I did have time planned earlier this week, but then a new laptop for me got delivered.
And I was busy setting it up, so apologies for that, but I will get to it shortly.
So, let me just note… Do we have Alexi here?
Guess not.
**Florian Lehner** 08:44 I think all the stuff Alexey had on the review items list are done.
**Felix Geisendörfer (Datadog, Inc)** 08:51 These are done, you think?
**Florian Lehner** 08:53 Yes.
**Felix Geisendörfer (Datadog, Inc)** 08:55 Okay, so I guess we shouldn't have copied that over, and just updates us up here, or…
**Florian Lehner** 09:00 I really moved.
**Felix Geisendörfer (Datadog, Inc)** 09:02 Huh?
**Florian Lehner** 09:03 I will remove it.
**Felix Geisendörfer (Datadog, Inc)** 09:05 Okay, yeah, I'll remove it here as well.
Okay, jonathan has an item on payload changes. Go for it.
**Jonathan Halliday (IBM)** 09:19 Yeah, that's the one that was do not merge for a long while, and it can now be merged, because we've introduced the diversioning model, so we can… break things.
So that just needs a quick one server, Approvals from people, and go in.
**Felix Geisendörfer (Datadog, Inc)** 09:38 Okay…
**Jonathan Halliday (IBM)** 09:41 Thank you.
**Felix Geisendörfer (Datadog, Inc)** 09:41 I won't.
I'm just doing a one.
Yeah, I will take a look, at some others here as well.
Okay, any… anybody have any thoughts on this one?
If not, we have to face the abyss of an empty agenda and ask ourselves if we want to make this the shortest meeting on record, or if somebody has, a topic that they want to bring up spontaneously.
**Josh Bonczkowski** 10:28 Not a topic, just wanted to introduce myself and a couple others that have joined. I'll even turn on my video.
Fair.
I am a human, not just a bot.
So, I'm Josh Bonkowski, I'm from New Relic, within the APM Plus organization we have there. We've been working on profiling functionality.
we're about to kick off, consuming the output of Profiling that I think most of this SIG is geared towards generating.
So that's why we're here, to kind of pay attention where the SIG is going, make sure we understand as it changes, so we can keep pace with what is happening at the same time.
there are a few others with me. Let's see, vinay, do you want to say hello?
**vinay NR** 11:26 Hi, everyone. This is vinay.
from Neuralink?
**Josh Bonczkowski** 11:31 And then we've got… Aravind, also here.
**Aravind Kumar Shenigarapu** 11:35 Hi, hi, this is Avin. I work on most of the backend stuff, for Profiling. So, vinay will be working on the front-end stuff.
**Josh Bonczkowski** 11:48 They're the ones that do all the work. I'm here for moral support, mainly.
**Felix Geisendörfer (Datadog, Inc)** 11:53 Cool.
Yeah, welcome to the Profiling Sig. Usually, we have much more topics to discuss, but yeah, you caught us on a very light agenda day. But I think once we sort of get through these few remaining items, just for context, we're getting pretty close to cutting our beta release for Profiling, hopefully we can get there before end of year. That's going to bring a new level of stability, and I think then we will start turning our attention to new areas in parallel to getting the signal stable.
Specifically, we need a simple allocation protocol for profiling, so when the eBPF profiler sends data, sometimes you get data with stack traces that are just numbers, which humans don't like so much.
And to get the file names and function names, we need a way to channel debug information from the build systems, typically, to the backends in order to make sense of the data. So that's going to be a new focus area, I think, for the CIC.
**Josh Bonczkowski** 12:56 Correct.
**Felix Geisendörfer (Datadog, Inc)** 12:57 So, you might also have to input insults on that as you… sounds like you'll be implementing support for ingesting the data, so you'll… you'll need something like that as well. Right now, all the vendors for your information have sort of developed their own systems of typically, like.
shipping the 12 sections of binaries to the backends in order to symbolicate. And maybe that's what we're going to standardize, but it's unclear. That's also discussion on Creating a more structured format for these payloads.
**Josh Bonczkowski** 13:25 Thank you.
**Felix Geisendörfer (Datadog, Inc)** 13:30 Cool. Any… anybody else? Any topics, questions, thoughts?
**Jonathan Halliday (IBM)** 13:38 Anyone planning to talk about this work at the Java Serviceability Meetup?
**Felix Geisendörfer (Datadog, Inc)** 13:47 I wasn't, but I guess if you're gonna be there, it would be really cool if you would talk about it.
**Jonathan Halliday (IBM)** 13:55 I don't know. It'll depend which day it's on. I might be on vacation already, but, yeah, if I'm there, you can…
**Felix Geisendörfer (Datadog, Inc)** 14:03 Marcus has already set the dates, he'll just have to reschedule it.
**Jonathan Halliday (IBM)** 14:08 I thought there was a poll open for it, last I saw. Okay.
**Felix Geisendörfer (Datadog, Inc)** 14:11 Okay, I don't know what the status is.
**Jonathan Halliday (IBM)** 14:14 Yep, yeah, I mean, it's a useful for them, because it tends to have the OpenJDK people.
At least some of them.
So it's… it's kind of worth… Trying to tie this into some of the, JFR, and I think the async profile of people sometimes come to that as well, so… It's a kind of point of overlap between different communities.
be worth, doing a quick session just to… Give people the lay of the land.
**Felix Geisendörfer (Datadog, Inc)** 14:45 Yeah, I think I'll talk to Marcus, I mean, he's my manager, so he'll bring it up, I'm sure. And if we don't have anybody, I'll make sure that one of us from Datadoc is going to talk about it, either myself, or Nayef, or… Yaroslav, we'll find somebody missing.
**Jonathan Halliday (IBM)** 15:04 Cool.
**Felix Geisendörfer (Datadog, Inc)** 15:06 Thanks for addressing it.
Cool. Any other topics? Okay, I see a hand, or did it disappear?
No, Boris. Hey.
**Boris Marinov** 15:22 I… so this time I'm unmuted in a planned manner. I have a… maybe, I don't know, misplaced question, but I'm not sure where to even ask it, so… A few months ago, I was working on some, like, integrations, and it occurred to me that resource attributes are nowhere to be seen in most front ends, right? So I started digging, and a thing that… maybe the polar signals one, and maybe the I'm not even sure if Datadoc shows this, but, like, basically, I can filter by attributes.
But I can never actually see what, without filtering, what attributes a resource, like a… like a… not span, what's the word?
carries, right? And I'm just wondering, is this, like, related to the storage engine, like, used in the background? For example, Grafana has its own thing, and maybe, like, group by is hard, but, like, is this a thing, or why is it not a thing? I'm not even sure who to ask. That's… that's what I was wondering.
**Felix Geisendörfer (Datadog, Inc)** 16:20 Is there a question about, like, why it's nowhere to be found, or about a specific vendor's implementation?
**Boris Marinov** 16:25 Well, it's a mixture of why is no one showing, like, resource… like, resource-level attributes, which are common for the whole, like, resource being displayed? And, maybe I'm missing something, or maybe it's… I think there are, like, two camps, the 99% of implementations don't show this, and then there's One or two, I need to… I wasn't ready for this question today, but I was just wondering, since… They're not alone.
**Felix Geisendörfer (Datadog, Inc)** 16:52 I think, and Nayef is here to probably shortly correct me and say how it really works, but on our end, when we receive OTLP data, we actually split the payloads into separate profiles, one for a process.
And each of those, profiles that the user can see in our Profiling list at Datadoc has the resource attributes. I think that's how we implemented it, so you can see them. Nayef, correct me if this is wrong.
**Nayef Ghattas** 17:17 Yeah, you can see them if you look for them, but in general, when… Customer, well, a user wants to look at, specific, at profiles. They want to look at profiles for a specific service.
So they filter by service, and they're looking at an aggregate profile across multiple pods of that service. So if we wanted to show resource attributes, we would show, I don't know, a list of, hundreds of, combinations of all the resource attributes for that.
**Felix Geisendörfer (Datadog, Inc)** 17:49 We actually do show in our aggregated view as well, now that you mentioned it, we have the facet on the left side, which shows you the dimensions, so you do have actually a way to filter by host and other resource attributes on the left side.
**Nayef Ghattas** 18:01 Oh, yeah, yeah, yeah, you're right.
**Boris Marinov** 18:03 So maybe it also requires you to group by that attribute, but not filter, so you can see all of, like, the groups. I think I have a feeling what the answer is. I've got to mute myself.
But this was, helpful. Thanks.
**Felix Geisendörfer (Datadog, Inc)** 18:22 Yeah, so I think that generally speaking, for people here who are looking into how to represent profiling data in user interfaces, I think it does make sense to surface resource attributes in various ways. The CAIC does not tell people how to do that, but just me, personally, I think it would make a lot of sense. I mean, otherwise, we wouldn't have to record some, and we spend a lot of time thinking on how to split things into resources. So, yeah, cool, thanks for bringing it up.
**Nayef Ghattas** 18:50 Yeah, but I mean, to be clear, it is, we need to surface them to be able to use them for filtering, but I think, the UI wouldn't be very intuitive if it showed all the resource attributes that are available for every query at the same time. For example, splitting the frame graph per all the resource attributes that are available would lead to a Playing up that would be hardly readable.
**Boris Marinov** 19:18 Yeah, yeah, I think you… what you can get away with is just group by one of them, but don't filter, like, let's say, say I want to filter by, let's say, some instance name, and I want to… that's… that works everywhere, but, like, grouping by instance name and seeing, like, okay, instance 1, 2, 3 of, like, my infrastructure, like, underlying infrastructure, like, semisimilator hosted I'm getting into specifics. This is what was what I was wondering, so it boils down to being able to group by by an attribute, like a… not distinct one, the opposite of distinct. Like, any attribute I pick, or not being able to.
**Felix Geisendörfer (Datadog, Inc)** 19:53 Yeah, so we… I don't think we have a group buy for our flamecraft visualization, but we do have it for our metrics, so if you want to get, like, CPU time by some attribute, I think you can do group by in our metrics here.
But yeah, anyway, I think definitely highly encouraged to allow people to slice and dice and understand resource attributes as part of user experience is the short answer here.
And if Andors don't do it, then… They should probably consider doing it.
Cool. Any… any other topics, questions, thoughts?
If not, then I promise to get my to-dos finally done until next time, and I thank all of you for coming here, for all the contributions made in the past, and getting us to where we are now, and yeah, then I wish you all a nice local time. See you next time.
**Florian Lehner** 21:05 Beautiful.
