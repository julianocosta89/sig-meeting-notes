SIG: Browser SIG
Date: 2025-08-28
Duration: 27 minutes
Zoom Recording URL: https://zoom.us/rec/share/0T69y9Vac3qCzX12EFbVtRYViLcQaB6rHK923NqIk70v640VR2uOOPcTRyLXRDnj.Z_I8052XnR3JQiRy
============================================================

## Zoom Recording Transcript

**Jared Freeze (embrace)** 00:37 Amen.
**Martin Kuba** 00:40 Hi, Jared.
How are you doing?
**Jared Freeze (embrace)** 00:42 Ed, thanks for your notes.
**Martin Kuba** 00:45 Yeah, I need to still go through it in a little more detail, but… Well, thank you for putting that together, that's… there's… Some really good information in there.
**Jared Freeze (embrace)** 00:54 Thanks. Yeah, we tried to, … just be specific, you know, because I feel like sometimes you just ask a bunch of questions, it's harder to generate ideas. It's like… it's always easier, I think, to just be like, I don't like that. What about this, you know? So… … But, … Yeah, I'm… I'm… and it already… it already sparked a good discussion about, the GitHub action, so I went deep on that. I think that might be the move, so… Talk about it here just in a second.
**Martin Kuba** 01:29 Yeah, cool.
**Jared Freeze (embrace)** 01:41 Is Ted back yet?
**Martin Kuba** 01:43 No, he's… Next week.
**Jared Freeze (embrace)** 01:47 Okay, cool.
**Martin Kuba** 01:47 Out for two weeks, yeah.
Alright, well, since Ted is not here, I'm just gonna… just gonna move… get us moving through the topics. I think we can get started, probably.
Jaredo, do you have the first item?
**Jared Freeze (embrace)** 03:06 Yeah, so I posted a link to, sort of the pitch for making a new repo for web.
In doing, the work there, I think I convinced myself of it, because I kind of wasn't sure at the beginning. If I had to do a TLDR, I'll give you the top three. If you just want to skip to the end, it's basically, like, what we should do. So my top three were, create a single convenience bundle, which has a single point of entry, so there's no dependency management. I think that's the big thing that everyone's worried about, is like, what version of core, what version of API, whatever it might be. If we just have a single package that just exports everything that we need, it'll be controlled internally, which I think is a little easier to understand for most people.
It may prevent people from using instrumentation in certain ways, … from outside the package in your app, TBD on that, but I think for a lot of people, it'll be an easy way to get started. Shared GitHub action will probably be the move for running the tests we need in the Node repo.
So I think if we just control, like, the integration test and the API test harness there, where it's running both basically both a piece of code, like repos, in… on both sides in GitHub Actions. If we can share that, I think it solves that. And then we just have to come to an agreement that our version numbers are not going to match.
with the JS repo, any longer. Don't know how we manage that, but I think part of the point of this is to move a little faster, which means we will presumably have more releases as we go. Maybe not all breaking, but I don't know if we can live with, like, 1.0 or 2.0 for You know, years at a time.
Cool, and that's it. So everyone, the link is there, and then, like I said, Slack or comment.
Thanks.
**Martin Kuba** 05:05 So, one question, Jared, I… you mentioned that there would be, we would have a single package that, includes everything, that users would… Would be, like, I guess it would pull in, like, the packages from JS and our instrumentations as well.
**Jared Freeze (embrace)** 05:21 Yeah, yeah, that was kind of the idea. So, yeah, really for convenience more than anything. So, that's not to say we shouldn't have, different entry points or different packages, just that we would have one just, like.
hotel web, that if you just want to get started, you start there, and you just import whatever, you know, all the sort of main stuff, basically. So that way, your peer dependencies never come up. You don't have to do, you know, install anything else, you know, in your… in your package. That's the idea.
**Martin Kuba** 05:53 Yeah, I just… I'm just mentioning that because I… I, like, I feel pretty strongly that, like, their users should have options.
Like, if they, like, some users may… Choose, like, nuts to include, for example, tracing.
So that their bundle is smaller, maybe they don't need tracing, but they care more about smaller bundle, so, you know, and just… just, like, collecting the basic events, so I think… Yeah, as long as we have that flexibility for users, then… Yeah.
**Jared Freeze (embrace)** 06:27 Yeah, as far as I have seen, the way things are laid out, it should be tree-shaken out.
If you have a good bundler. If that's not the case, then I think that's solvable, so we'll just figure that out.
**Martin Kuba** 06:40 Okay, cool.
Okay, so the ask here for everyone is please take a look at the doc and comment. They would like to make a decision on this soon.
All right, I do have a… I do want to walk through the board, but I think we can just do it at the end.
I think the next… looks like the next topic is for Abinet?
**Abinet Debele** 07:14 And I think I, I think I, I know, and I can actually speak to that too, but go ahead, Eminent.
Yeah, I see that you have discussed this one before in this, meeting, and, there are some suggestions on the PR tool, I can see them, and I just summarized the changes suggested here, and we can… I wanted to know if you can discuss it, and, probably finalize, Same amount of commission, yeah.
**Martin Kuba** 07:40 Yeah, it's… it's… this isn't my, this is for my to-do, … I, yeah, so I do… what I need to do is, we have that page view.
Page view semantic conventions, which were defined as body fields, and we're getting away from body fields.
So I need to update that PR to, define separate list of attributes. It's not a good… attributes, and just have.
**Abinet Debele** 08:06 Yeah, I have already mentioned it here, like, the attribute… under the attributes, I have mentioned all the values.
**Martin Kuba** 08:12 They are to be moved to… from Badi, right? I've mentioned that in the….
**Abinet Debele** 08:16 Code, here, yeah.
Can you share the document?
**Martin Kuba** 08:21 Yeah, I'll share my screen on….
**Abinet Debele** 08:36 Yeah, … So I… I've actually summarized this on the… on the… Meeting document itself, so you can….
**Martin Kuba** 08:45 Okay.
**Abinet Debele** 08:46 Yeah, if you see that on… the attributes, under attributes, I've mentioned the values. I've mentioned that they are to be moved from body.
The URL full, that's the name suggest for the URL?
I think we're… we're gonna keep the referral.
And for the type, there are changes suggested, whether it should be hard or soft, or page load, or raw change.
And, the state change is also changed from… it was changed state, now it is state change.
So we have values of push state or replace state.
Yeah. I've seen someone suggesting whether it should be just push or replace, and… Yeah.
And the title is… suggests to remove the title, so… … Yeah, my ask is, can we just… Confirm these changes are the last ones, or do we need other changes, too?
**Martin Kuba** 09:39 Yeah, I'm not… I think… so I… I… to be honest with you, like, I have to look at what others have done on this, but I think what we need to do is, like.
I'd add, like, Attributes that have the full namespace.
And then there are just referred, like.
You know, referenced in this event.
So, like, it's… it's not gonna be just referrer, it's gonna be, like.
I don't know, browser, page view, data referr… … So that's what I need to figure out, like, what those attributes are gonna be called.
And where they're gonna live?
**Abinet Debele** 10:16 Okay.
**Martin Kuba** 10:16 Yeah, I do agree with you. Yeah, essentially, this is what we need to do, yeah. We need to move them out of the body and make them… Regular attributes.
**Abinet Debele** 10:28 Okay, yeah.
**Martin Kuba** 10:30 Yeah, so this is, like, this is, like, on the top of my list, I've been at, so, like, I… I'll work on that, before next meeting for sure, and… I will ping you, like, once.
Once… so that you can update your, your, instrumentation.
**Abinet Debele** 10:46 Alright, thank you.
**Martin Kuba** 10:54 Okay, … Does anyone have any questions about this?
Okay, cool.
Is there any other topic?
That anyone wants to talk about before we get into board review?
**Joaquín Díaz** 11:08 I think it's kind of related, like, last time, We discussed about the… This, like, information that we want to get from the browser on my… the document that we shared together.
I think the idea was to… Get, like, a list of things that we want to split into, then working into the model, the observability model for each one.
I don't know if you've had a chance to take a look, or we want to decide at least one of those things.
For a few things here. I know, for example, page view is going to be useful. That is some of the work that we will need to do for other modeling.
… But yeah.
So I'm opening the document again. Like, we have page load, we have sessions, we have net of requests and user interactions.
My idea last week was, if everyone agrees on that's what we want to get from the browser, that we split those four into, like, tickets or hours called in GitHub.
And we start actually writing like, how it's going to be instrumented, like, whether it's a span on an event that the attributes that will have, and everything that we can get.
Yeah, I don't know if we are okay with that information. Should we move on with, like, actually working on it?
**Martin Kuba** 12:36 Yeah, agreed, so I think… I don't know, has there been any more discussion on that document that you shared, Joaquin?
**Joaquín Díaz** 12:43 No.
**Martin Kuba** 12:44 No.
… So, I mean, it looked good to me. I suppose if there's somebody here, like, who hasn't looked at it, and you, like, you're interested, like, in working on instrumentations, please take a look at it. But in general, I think that's the direction that we… But it sounds like that's where you want to go, in that direction.
… And I actually saw, like, looking, looking at the… let me open the board.
Fair.
**Joaquín Díaz** 13:13 Yeah, I think there are some things on the board that may match to, like, the items of the document, so, maybe we don't need, like, 2K tickets for everything, but… like, I'm sure if, for example, ad browser page, or span event, that is, I think, one of the most important ones.
Then there is one for reception as well, so I think some of the stuff is already here. User action is also there.
So yeah, if you… If we all agree that that's what we want, then we can maybe start, like.
assigning or thinking who can work on these tickets. I'm happy to take one of them.
**Martin Kuba** 13:52 Yeah, yeah, that sounds… sounds good.
… Yeah.
So, so we have… We have a couple, like, we have a few issues already, for semantic conventions and instrumentations that I created a while ago.
… And then we have some of these just tasks that I think… Ted created.
So we should, … Yeah, for any of these that actually don't have issues, maybe, like, we should just go ahead and create issues.
But from what I can tell.
So the ones… the ones that we actually have, like, we have… The… for semantic conventions.
Like, we have the… this is the page view.
1… That Abinad was talking about. It says that it's done, but it's not done.
This is… this one is actually… this one is in progress.
… So that's the one that Advent was talking about, and the corresponding instrumentation is here, this page view, event instrumentation.
that Eben is working on.
… I think in your doc, you for sure had errors. There is, … There is an existing PR to add event for errors that Pervy is working on.
And I don't know if Perg is here, but, there's… There is, … on that PR….
**Wolfgang Therrien** 15:29 Yeah, I'm… I can take that over for… for purview. I can follow up on that in the next week or so.
**Martin Kuba** 15:35 Okay, perfect, yeah, there's some… there was actually some requests for changes, so… Okay, cool.
… And then… There's semantic conventions for user Action… Let's see… There's, right now Carly, I don't know, like, is Carly here?
Yeah, so I'll reach out to Carly, But if she's not able to continue with this, then maybe you can assign it to someone else.
**Joaquín Díaz** 16:15 Hmm.
**Martin Kuba** 16:16 … There is worse resource timing.
So, I don't know, like, this… ….
**Joaquín Díaz** 16:27 That, in my mind, that's, like, a subset of the Patriots fan event.
I don't know if that's the same thing that I'm Thinking all that, can you open the company description?
**Martin Kuba** 16:38 He said, like.
**Joaquín Díaz** 16:40 Yeah, for every resource at the web.
They were also… Or what was the idea?
**Martin Kuba** 16:48 I think this idea is to, … to collect events for, you know, from the resource timing API, for, like, for network requests.
**Joaquín Díaz** 17:00 Okay.
specific for resources, or for every request, like, also, like, APIs and….
**Martin Kuba** 17:10 Yeah. That's tough.
Yeah, all those, yeah.
All of those.
**Joaquín Díaz** 17:16 And, don't we have the batch instrumentation already there?
Or it's not the same… I mean, it's not the same way of capturing, but at the end of the day, it's a network request, right?
**Martin Kuba** 17:28 Yeah, so this is… I don't know if we need this, I don't… … you know, maybe we should… I don't know, so I think we have… we have to fetch instrumentation currently that, … Uses generated spans.
And if you also have the resource timing.
Event-based instrumentation, then it doesn't seem to me like we would need a separate fetch timing event.
Because you would get that from the resource timing.
**Joaquín Díaz** 17:58 Yes.
**Martin Kuba** 18:00 So I think this one probably… is not needed.
… the….
**Joaquín Díaz** 18:09 Do we have any description on the ticket, on, like, what was expected?
Yeah, I didn't create this one, so I… Okay.
**Martin Kuba** 18:17 … … the page load span event, that there's also existing instrumentation in contribib, jscontrib, that generates The page load span.
**Joaquín Díaz** 18:32 Yeah, the documental disfrontation.
**Martin Kuba** 18:33 Document load, yeah.
So, like, I don't know, like, if this would be different, or….
**Joaquín Díaz** 18:40 We actually even… we forgot that one recently to add more stuff.
I think we can't take it, … like, as it is, it works, but we added more stuff that is newer, from the API, like, … The transfer size and, like, whether it's not cache, if it is blocked or not, some… just some attributes.
But I don't know, like… if the… like, all the attributes are based on HTTP, and there are more attributes, and I don't know if we want to add to that convention, or we need, like, a new convention for… like a resource fetch, for example. So that document load instrumentation, it produces a document load span and a resource fetch span.
Which some materials are coming from the HTTP semantic conventions, but some… the ones that we want to add are new.
We actually don't know where they should go. Like, do we need a new I don't even know how it's called, but do you need, like, a new… not entity, I know entity is something else, but we need something new that is called a resource fetch, or… document that or something, or should we keep adding attributes to the HTTP namespace?
**Abinet Debele** 20:00 I had, just a question here, is the page load spun event? Is it an event, or a spawn, like, it's… The name is….
**Joaquín Díaz** 20:08 I know it's just fun. The… Sorry, I… I don't know, this is rough, but what we… what currently is on the document… on the document non-in instrumentation.
**Abinet Debele** 20:18 3 sets of window.
**Joaquín Díaz** 20:19 sponge.
**Abinet Debele** 20:20 It's currently Hispania, but I mean, we are trying to create an event now on this one.
**Joaquín Díaz** 20:27 I think the idea was to move towards events and just have the duration as an attribute, right?
**Abinet Debele** 20:34 Okay, okay.
So the spawn… is the spawn required, still in the name? Pageload spawn event?
**Joaquín Díaz** 20:42 That's a discussion that we need to have, actually, like, how do we want to capture this?
**Martin Kuba** 20:49 Yeah, this is a little bit confusing, because we have the page view events, we have the navigation timing event.
**Abinet Debele** 20:57 And then this one says event, but I think it's supposed to be span.
Oh, okay.
**Martin Kuba** 21:04 That's what I would expect, yeah.
**Joaquín Díaz** 21:07 I can take care of that, I will… maybe I can propose both options, whether it's a span or an event, and … We can decide.
But I think we should… Take a look at everything together, like… If, like, page load should include.
… They… some resource fetching timing, they… Because, see, all these resources are what are adding time to the page load.
like, doesn't make sense to me to look at facial without looking at what resources are fetching, or what API calls are doing.
… Yeah, I can take a look and try to.
I, you know….
**Martin Kuba** 21:50 You know, I….
**Joaquín Díaz** 21:51 But they don't have, like, a more, like, big picture.
View, and we can decide it later.
**Martin Kuba** 21:58 Yeah, yeah, so I think… so we had those two documents, your documents that… kind of shared, like, the… kind of, from users' perspective, what data we want to collect, and I also had that… I also had a separate document where I think my… my document was more focused how So maybe we should combine those two, and, like, have a discussion on, like, how… what kinds of instrumentation.
**Joaquín Díaz** 22:23 Yeah.
**Martin Kuba** 22:23 We want to have. And then, like, then, like, make sure that it aligns what we have on the board, yeah.
**Joaquín Díaz** 22:31 Yeah, okay. Yeah, there's also… you share a few spreadsheets with all the attributes that other vendors are already capturing.
We can also combine with that now that we are looking into attributes and see that we're not missing something.
**Martin Kuba** 22:47 So why don't I… I mean, I think this is pretty, pretty important, because, … Like, we're not… like, if anyone wants to contribute, like, people are looking for things to contribute, like, we wanna have, like, defined… defined, Task, or instrument… specific instrumentations for people to work on.
So what I would… again, I think if nobody has looked at… there are some folks that haven't looked at this, please do. Like, I don't… what was it, … yeah, it was this doc, right?
So I'm just gonna….
**Joaquín Díaz** 23:17 That might be… so that is the one that has, like, a mix of telemetry and the information that we can have from the browser, but then if you see the other one is real user monitoring, the one below that.
Sorry, above that, on the net.
This one. Yeah, that one. So that one is only… Like, from the user's perspective.
**Martin Kuba** 23:40 Okay, I'm just gonna put this here, like, as a….
**Joaquín Díaz** 23:43 Hmm.
**Martin Kuba** 23:44 … Yeah, and so that was this one.
**Joaquín Díaz** 24:09 Yeah, I'll give it a try to page load spam.
It's weird that it's called Pagelo spun event.
… I will give it a try. Maybe, like, I… yeah, we can see later if we need to redefine some tasks.
But yeah, based on your dog, that has more the modeling than the other… Spreadsheets of, vendors.
Yeah, Econavia's fine.
**Martin Kuba** 24:38 Okay.
Cool.
… I also wanted to point out… One more thing here… And that's, … I had… I had this work in progress for a while, which is adding a prototype for For, like, a session manager interface, or implementation.
… it looks like, actually, it's very, very close to, like, being able to be merged. There are a couple of… updates that I need to do, but it looks like… … the JS maintainers are fine with merging this, … But I want to make sure that Folks here are okay with merging this, … So, like, again, like, I'm just gonna ask one more time, please take a look at this. I mean, if you, like, if… obviously, like, session… session, like.
Session management, like, is really, really key for us. … So, like, do we want to have… this kind of defines… this is a prototype for… How users would interact with sessions.
And how, like, imp… imp… how… Our storage and session duration would be implemented.
So… if you're working for a vendor, like, who would be, you know, interested, like, in session… capturing sessions, please take a look at this before it's merged. I mean, we can still make changes afterwards, but, … Yeah So I'm just gonna… Also… Ask for review here.
Okay.
… Yeah, that's probably… All that we can do right now.
Does anyone have any questions or comments?
Here.
Alright.
Like, so I guess the next, next steps, discussion on… We have the discussion on the separation of the repository.
We have, also discussion happening in… around the data model.
Which would, … Then help us define the tickets properly.
And also, Briset, you can… Take a look at the session manager.
**Joaquín Díaz** 27:29 Yep.
**Martin Kuba** 27:30 Alright, well, I think we're done then. Just about time, so… Thanks, everyone.
