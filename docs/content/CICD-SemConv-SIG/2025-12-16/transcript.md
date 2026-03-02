SIG: CI/CD SemConv SIG
Date: 2025-12-16
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:41 Hello?
**Johannes Koch** 00:43 Hello, Christoph.
You're French, right? What do I do?
**Christophe Kamphaus** 00:48 Luxembourgish.
**Johannes Koch** 00:49 Luxembourgish, but you speak some German. No, you don't.
**Christophe Kamphaus** 00:52 Yeah, I do.
**Johannes Koch** 00:53 Okay, I'm from Germany, so… I've seen your name around, but… but we haven't formally met, so…
**Christophe Kamphaus** 01:00 I saw you in the recordings, I watched some.
**Johannes Koch** 01:03 You did? Okay, cool. Then you know that I…
But I'm, at the moment, still looking. I'm gonna get there somewhere later.
**Christophe Kamphaus** 01:14 Hi, Atria.
There seem to be connection issues.
**Johannes Koch** 01:39 Well, you never know where he is and what he does.
**Adriel Perkins** 01:46 Good morning, or day.
**Christophe Kamphaus** 01:49 Hello?
**Adriel Perkins** 01:51 How are y'all?
**Johannes Koch** 01:55 those two… break, I think.
That's how we call it.
**Adriel Perkins** 02:03 Cool.
**Johannes Koch** 02:04 What about you?
**Adriel Perkins** 02:07 Chilling. Literally. It's cold.
**Johannes Koch** 02:11 How cold is it over there?
**Adriel Perkins** 02:13 Today is better. Yesterday, it was 3 degrees.
**Johannes Koch** 02:18 That's cold.
**Adriel Perkins** 02:19 Fahrenheit, yeah. Yeah, it was chilly.
I'm already looking forward to… Summer.
The problem is, is that we haven't even hit winter yet. We're technically still in fall.
**Johannes Koch** 02:46 That is true.
**Adriel Perkins** 02:58 Alright, got the agenda up. Feel free to…
Put down anything you'd like to put down?
Brr.
Well, whatever. I'll just click it this way.
Alright, we can start by going through, the board.
I only have one main update on the board.
the, SDK… oops.
the SDK, issues… I opened up the issues for the ones that are not stretch goals.
Trask is working on moving them over to our project to make sure they do show up on our project holistically, but right now, I've got them linked as sub-issues inside of the implementation issue tasks.
Section. And so these are the various different issues. Anyone's more than welcome to add additional contacts, but I kept them very simple. Basically, support the spec.
So, I would ask, if you can go through these and just give a thumbs up to them, that would be good. I know we are gonna be primarily
Well, maybe, primarily, actually implementing some of these things.
It'd still be good to give the thumbs up, just so it's, like, clear that it's, like, this is a wanted thing here.
**Johannes Koch** 04:51 Okay, so you went over and created the stories in the other projects, okay, yeah, got it.
**Adriel Perkins** 04:57 Yep, yep, created issues in each of the repositories, and then just linked them to this main issue inside of our Phase 2 project.
**Johannes Koch** 05:06 Okay.
**Adriel Perkins** 05:18 And then Trask is working on getting these to show up in our project board directly, so they'll show up under, like, in progress and whatnot, so we can track.
**Johannes Koch** 05:27 Okay.
I just had one question on 2124, Christoph, maybe something, kind of, you're linked to stuff that the… what is that CD Foundation at the end? Is that, like, another open source project? Can you just explain that a bit, so I understand that a bit better?
**Christophe Kamphaus** 05:52 I'm not sure how the CD Foundation is related to the CNCF. As far as I know, it's independent.
**Johannes Koch** 05:59 Okay.
**Christophe Kamphaus** 06:00 And they did some, specification work around CD events.
**Johannes Koch** 06:06 Okay.
**Christophe Kamphaus** 06:07 The semantic conventions technically support, because they do have some semantic conventions for CD events.
**Johannes Koch** 06:17 Okay.
But essentially, it means that this should be pretty simple, right?
This is, like, a write-up.
Of mapping the pull requests to…
And the actions to the different Vendic convention terms that we have, right?
**Christophe Kamphaus** 06:38 Exactly.
**Adriel Perkins** 06:39 I don't know if it'd be Go ahead, sorry.
**Christophe Kamphaus** 06:42 We took also some of the terminology from CD Foundations, the specs they had there.
We, of course, adapted some because we were not mainly based around events.
And, yeah, so you have this…
Page where they compare the different tools and how they relate to their own terminology.
So I thought we could do something similar.
In semantic conventions.
**Johannes Koch** 07:16 Okay, I got it, thank you.
**Adriel Perkins** 07:20 Yeah, when we originally opened up the very, very first issue for, a proposal for attribute conventions, we actually heavily utilized the CD events.
We determined, based off of community questions, this was the original proposal, community comments, rather, we decided to not go with any of those, and instead.
rename all the attributes to map what would be agnostic, because CD Events is heavily inspired by Takton Pipelines. So a lot of its nomenclature comes directly from that opinion, and we wanted to make sure that we were kind of agnostic of any underlying tool.
And we, as Christoph mentioned, weren't really focused directly on events first. We were focused on the attributes in the registry as a first place to start.
I… because of that, and because of just the history of this issue, and how it went down, like, we spent a bunch of effort, really, like, coming up with this proposal, and then basically it got thrown out, and, like, had to, like, re-change it entirely, which was good, because…
I mean, that's how you get dialogue, and that's how you figure out the right path forward. But just based off of that, my guess is this is probably not going to be necessarily quick.
**Johannes Koch** 08:39 Oh, great.
**Adriel Perkins** 08:39 be simple, but, like, we're definitely not going to use…
there… or we're not likely to use their terminology, we're still likely to use the attributes that we've defined in the registry, but we may be able to do… try to figure out where there's overlap, to make things useful.
**Christophe Kamphaus** 08:59 Definitely where it maps to tool namings, because those are the same.
And so it would only be a matter of using our own terminology.
**Johannes Koch** 09:11 Yes.
Now, my next question is gonna be, why did we create that story for GitHub only, Christoph? Because we need to do that for the other providers as well, or not.
**Christophe Kamphaus** 09:23 Exactly.
**Johannes Koch** 09:23 Okay.
**Christophe Kamphaus** 09:24 I think at the time, we only had the GitHub one, pause.
**Johannes Koch** 09:28 Sorry, very… as I said, Giannis.
**Adriel Perkins** 09:30 Oh.
**Johannes Koch** 09:30 Stupid thing.
**Adriel Perkins** 09:32 I'm sorry, so this is the one that I'm talking about that's general and agnostic and talking about events as a whole. Okay. This one is actually…
**Johannes Koch** 09:42 That's the one I would.
**Adriel Perkins** 09:43 This is different. This is not CD Foundation stuff. This is adding GitHub-specific attributes. I'm sorry, this is helping people to understand what GitHub attributes map to, what OTEL attributes, or GitHub names map to OTEL attributes.
**Johannes Koch** 10:01 Yeah, and I think that's what I understood from the description as well, and I was just trying to make the connection to the CD Foundation, and then at the end, the comment is like, okay, we need to do that for GitLab as well, for Jenkins, and for others as well, right?
**Christophe Kamphaus** 10:14 Exactly, and I think on that page they have there…
So you already did the mapping for the different tools, so that's what I want to say. We can take that and just replace their terminology with the…
**Johannes Koch** 10:30 Yes, I got it.
**Christophe Kamphaus** 10:31 To that one.
**Johannes Koch** 10:31 So I think, Christoph, you and I were talking the same language, just Adriel was talking about the other story.
**Christophe Kamphaus** 10:39 Got it.
**Adriel Perkins** 10:39 In any case, I think we can adapt here as a description to make this clearer.
**Christophe Kamphaus** 10:43 that it's not just for GitHub.
And we can include GitLab as well.
**Adriel Perkins** 10:49 I mean, this one was specifically for GitHub, because the ask came from the community, because they didn't understand, like, the GitHub receiver's attributes and how those map over. I think if we want to do one for GitLab, we should probably make it in a separate issue.
**Christophe Kamphaus** 11:04 Maybe you can open the page from the CD Foundations?
**Adriel Perkins** 11:11 one.
**Christophe Kamphaus** 11:12 It's the same one, it shows different places.
It's the same page.
**Adriel Perkins** 11:18 Got it.
**Christophe Kamphaus** 11:23 Yeah, so you have there the mapping of terms, it's just a big table.
And Sana Buffett.
They go into a bit more detail for the different tools.
**Adriel Perkins** 11:37 So, I guess you're thinking, like, create a generic mapping page, and those…
**Christophe Kamphaus** 11:44 Just to include… okay, I'm not sure how that will…
**Adriel Perkins** 11:52 work… we'll need to figure out how that will work, with the Weaver stuff, since Weaver does a lot of the code gen and table gen.
**Christophe Kamphaus** 12:00 I think sister.
a pure doc page, so nothing in Weaver, nothing in the model, it's just some, mapping…
I think there's also other conventions that do similar stuff, where they just do descriptions or mappings to other…
**Adriel Perkins** 12:20 Yeah, I mean, the way they… the way that we've done it in Weaver in the past is, like, you'll have,
Like, if you go to Azure Events.
No, actually, what was the database one? That's the one that I want. Yeah, so, like…
You actually have, specific conventions…
Well, so this is a kind of a combination of the two things.
You have specific technologies which have their own sets of conventions, so there are some GitHub attributes that aren't gonna map to OTL attributes, and that's, where these could live. But in terms of…
**Christophe Kamphaus** 13:02 Basically, vendor extensions.
**Adriel Perkins** 13:04 Yep.
I don't know if we have precedent for just raw mapping that's not a vendor extension.
I'll have to go revisit my…
Well, do I not include that? I know in the hardware semantic conventions, they had some notes how certain values can be computed.
**Christophe Kamphaus** 13:30 But that's not really what we…
Would have in, this kind of map… terminology mapping.
**Adriel Perkins** 13:39 Right.
Alright, so we'll need to kind of figure out a couple things, then.
**Christophe Kamphaus** 14:13 I think just browsing the also… conventions.
some of them do have pages where I don't see right away.
Just with our models being auto-generated.
For example, generative AI has LLM call examples.
So I think it would be fine if we had a page just describing the mapping between different systems.
Of course, it would be better if we could have vendor extensions, but we also take
additional details and defines them into semantic conventions. I think that would be ideal.
And I… that's an… Another issue I think we have on our board.
**Adriel Perkins** 15:12 Yes.
**Christophe Kamphaus** 15:13 Yeah, it's the 1193.
And I think this task we were discussing now is purely documentation.
**Adriel Perkins** 15:27 Okay.
**Johannes Koch** 16:02 And essentially, that means only writing Markdown, right?
**Christophe Kamphaus** 16:06 Yeah.
**Johannes Koch** 16:08 And just… still learning. I would need to fork semantic conventions, create the new Markdown file.
or multiple ones, depending on how we want to do that, and then write down the mapping. That's what we would want to do, correct?
**Christophe Kamphaus** 16:28 Yeah, I think to get started, it would be just a single page.
And then later, if we have under-extensions there, I think we can split it up like it's been done for databases.
**Adriel Perkins** 16:45 Alright, does this comment make sense? Is there anything I need to change based off of our conversation here?
**Christophe Kamphaus** 16:52 Well said.
I have a question. Do we have a winter break over the next few weeks now?
**Adriel Perkins** 17:35 Yeah, I think so. I think, I think that was what, well, there was,
Is it in the… We talked about this, yeah, here we go.
So, December 22nd through January 2nd.
**Christophe Kamphaus** 17:58 Okay, so… Next two weeks.
**Adriel Perkins** 18:01 Yep.
Alright, cool. So I'll make… what we'll do for an action item is just…
Post that in… oh, wrong thing.
**Johannes Koch** 18:54 You usually, yeah.
**Adriel Perkins** 18:59 We'll post… make a post on that.
Alright.
Cool. Let's see, any, agenda items that anyone wants to talk about?
Other than that…
Oh, actually, I guess on the board, I will say one last thing for visibility on my end is that I have been heavily working on maintenance of the GitHub receiver. There's been a few outstanding issues that have been opened up.
As it relates to, metric issues for scraping, we did have one person open up a contribution, which was really cool. They just…
shipped it.
And it was to fix the span relationships based off of the semantic inventions.
So that was actually, like, really cool. You know, people are paying attention, which is… which is very nice.
And so, I've been mainly focused on maintaining that for the last little bit, and I'm gonna be adding log support as well, so that all the events that come from GitHub can be transformed, so that the work on that mapping is gonna be pretty, pretty nice, and,
Congruent to that effort, so that's gonna be good.
Really?
**Christophe Kamphaus** 20:47 I think that was a long-standing request.
**Adriel Perkins** 20:50 Yeah, yep, for sure.
**Carlos Alberto Cortez** 20:54 Is there some kind of issue for that, or multiple issues tracking that? Or is that something that you're doing on your own?
**Adriel Perkins** 21:02 It's a little bit of both. So it's mainly an open telemetry collector contrib issues that have been opened up that I've been fixing and maintaining. But in terms, yeah, so there, there are…
issues open in Hotel Contrib that relate to those items that I just talked about, yes.
**Christophe Kamphaus** 21:22 Would it be possible to add some here on the board?
**Adriel Perkins** 21:26 Yeah, I can see if I can get Trass to add them, A problem is, is… well…
Yeah, the problem is, is, like, there's always issues on that board, so it's like…
The only people that can seem to be able to do it, like, to move those things are, like, maintainers, so…
I can take an action item, though, to see if it makes sense to move them over. Or maybe I can just create… actually, I'll tell you what I'll do. I will just create an issue similar to this one.
that talks about maintenance, and I'll just link the different issues in here so that there's a long-standing list that gets checked off as I go. And that way, I don't have to actually add them to the project, because they can show up from this one issue.
Like, none of these are currently in our project, they're all in their respective repositories, but they still show up here and are linked. Does that work?
**Christophe Kamphaus** 22:25 Yep.
**Adriel Perkins** 23:04 All right, cool. Anything else anyone else wants to talk about?
**Johannes Koch** 23:09 Nope.
**Christophe Kamphaus** 23:10 Nope, not from my side.
**Johannes Koch** 23:13 Have a good Christmas time.
**Christophe Kamphaus** 23:16 You too.
**Adriel Perkins** 23:17 Cool. We'll see you out there, y'all.
**Christophe Kamphaus** 23:19 Are you into next year?
**Johannes Koch** 23:20 Bye-bye.
**Adriel Perkins** 23:21 I…
**Christophe Kamphaus** 23:21 But…
