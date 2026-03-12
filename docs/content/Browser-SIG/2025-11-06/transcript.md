SIG: Browser SIG
Date: 2025-11-06
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:36 Hello?
**Benoît Zugmeyer** 00:39 Hello?
**Marco Schäfer** 00:51 Hello!
**Benoît Zugmeyer** 00:55 Yep.
**Jared Freeze (embrace)** 01:34 Hey, everybody.
**Marc Pichler (Dynatrace)** 01:36 Hello?
**Marco Schäfer** 01:38 A…
**Martin Kuba** 02:11 Bye, everyone.
How's it going?
**Jared Freeze (embrace)** 02:16 Hey, what's up?
**Martin Kuba** 03:01 So, Ted is not here, And we're a few minutes over, so I think we can probably get started.
**Jared Freeze (embrace)** 03:09 Sounds good.
**Martin Kuba** 03:12 Okay, I can just go through the, through the agenda. First one is Trask. Trask is not here, but I think he's just, Telling us to come to the, someConv.
meeting, which would be in 2 weeks, I guess?
Yeah, we're weak.
Week and a half.
**Daniel Dyla (Dynatrace)** 03:35 Yeah, I think everything next week is likely canceled because of the, KubeCon, at least all of the project-wide, non-SIG-specific meetings. SendCon and spec and such.
**Martin Kuba** 03:49 Right, okay.
Okay, the second topic is Mark.
**Marc Pichler (Dynatrace)** 03:56 Yeah, so I'm not fully up to date on what the status is where browser packages will go, but I talked to the other maintainers, the JS maintainers, about how we could unblock some work that BrowserSig is doing.
And, came up with an idea to make the browser-Sig maintainers approval equivalents in the JS repos for the packages that are browser-specific.
So that would be, let's say, any browser-specific instrumentations in the contribo, and also, yeah, in the core repo, let's say the webcommon, and stuff like that, so that y'all can move a bit quicker there, and are not limited by reviews, from Us.
Because it's very, obvious, always, that reviews are always the bottleneck, right?
And you have the most, context on all these things there, and the know-how. So, yeah, just reaching out, seeing if anybody is opposed to doing this, or if there's any concerns about this at all.
**Martin Kuba** 05:12 I think that's a good idea, thanks for suggesting that, yeah.
**Marc Pichler (Dynatrace)** 05:17 Alright, Yeah, I will, then probably just open a PR on the JS repo to add that to the README, and then I can also go through and, add everybody, to Code Owners and in the admin repo.
Should be fairly straightforward to do that.
I already talked to everybody, of the JS maintainers, and everybody's on board, so it should be very smooth.
**Martin Kuba** 05:47 Awesome.
I actually have a, related… Question or topic for discussion?
So I see that we are already in a… Place where we are thinking… we are introducing new packages.
And they're… they're… Going into the browser repo.
So now they'll be kind of split between 3 different repositories, and… Since you're suggesting, like, that we continue to, like, you know, being approvers… approvers in… the contribp and JS repos suggest we would be continuing to maintain them there. I guess my question is, like.
Do we want to move all the web packages to the browser repo?
Should we do it now? Should we do it over time? Like, when? How should we do this?
**Jared Freeze (embrace)** 06:36 My… my opinion was that we… so there's still PRs in flight in those… in the two, you know, current repos. I think it was, like, get those through, and then try to migrate once those are sort of stabilized with the changes that we had already you know, that started well before we had the SIG. So, that was my idea. I don't know how everyone else feels, but, yeah, the migration, I thought, was, you know, the point, right? So…
**Wolfgang Therrien** 07:02 Yeah.
I agree with that. I think also now that we have a little bit more maturity in, the browser repo, right, we have a little bit more, like, tooling there, I think it makes more sense to think about what our migration plan is.
**Daniel Dyla (Dynatrace)** 07:19 Yeah, it's probably on me for not bringing the plan back to the JS SIG, as much as I should have done.
I've had an internal job change recently, and haven't been as active over there as I was in the past, to be determined how permanent that situation is.
So that's probably on me, but yeah, Mark, the plan is to move everything to the new repo.
**Marc Pichler (Dynatrace)** 07:46 We'll have to look into how we are gonna handle publishing then for that.
**Daniel Dyla (Dynatrace)** 07:52 Yeah.
**Marc Pichler (Dynatrace)** 07:53 Yep.
**Daniel Dyla (Dynatrace)** 07:54 Especially for SDK packages, Because the… the version locking turns out to be extremely important for users to not be totally confused all the time.
Like, the version numbers, even if things are compatible across versions, which they typically are, users just cannot figure out what versions of stuff they need to install unless the version numbers match exactly.
So for… if you're gonna have, like, a… SDK package for the browser.
it needs to match the version exactly of the… of the main SDK, or, like, it doesn't need to, it just will cause less confusion in our experience.
**Jared Freeze (embrace)** 08:40 Yeah, I propose that we have a single point of entry for the browser repo, so that you're not managing… like, you want to include API logs, like, if you're using web, right? It'll be embedded in the package, and then you'll just have all the exports there.
that conversation hasn't got very far, I just thought it was a good idea, so it'll get on the agenda eventually, but, that was… something, you know, we've experienced, you know, as well, right? Like, oh, we gotta bump this, but not this, or, you know, whatever it might be, so…
**Daniel Dyla (Dynatrace)** 09:09 So you're saying that the SDK, or that the instrumentations would call that entry point package?
**Jared Freeze (embrace)** 09:17 The idea would be, you know, at hotel selector? Or just for any everything comes out of there. We could also export subpackages, so it'd be, you know, at OpenTelemetry slash browser slash document load instrumentation. So, I think we could do both. So, most people would probably use the main entry point, so once you're… you know, pulling out document-led instrumentation, which is also available there, you're not managing what those depend on, right? So, if you bump open telemetry slash browser, everything goes with it. Now, if you need to change things, they all come together, so…
**Daniel Dyla (Dynatrace)** 09:57 Okay, Yeah, okay. I don't have anything to say about that right now, but I believe that that… is not… In line with the specification.
Which requires the separation of the API and the SDK pretty explicitly.
And other languages in the past have tried to do what you just said, and have been told no by the TC. So, I just… be prepared for that discussion, I guess.
**Jared Freeze (embrace)** 10:29 Cool. Thanks for the background. Yeah, I'm… I'm new here, so kind of figured it all out. Cool.
Looks like, Joaquin, you're up next.
**Martin Kuba** 10:46 Actually, I have one more thing. So Dan, you said that you had some plan?
For the, for, for the migration, or, or some, some thoughts?
**Daniel Dyla (Dynatrace)** 10:54 Me? Yeah, so we've done some repo migrations in the past. People who have been around JS know that we… the contrib repo didn't always exist. API used to be in its own repo, and we moved it into the main repo. We've done a few of these migrations, and in my experience, unless you have, like.
very, very active PRs with dedic- with, like, specific end dates targeted for them, and people working, like.
synchronously in meetings on getting them merged. Waiting for them to merge is, like, you're gonna be waiting forever. So what we did in the past is just, you know.
cut it off, say, please reopen in the new, repo. We linked in the descriptions back to the old version of the PR, so it would be like, any, you know, there is some previous discussion here.
with a summary of what the main discussion points are, and just reopen stuff, because we found that PRs were just dragging for months and preventing our migration.
So, that would… my recommendation would be to just do it, unless you have spec… like, a very small number of specific PRs that you're hyper-focused on.
**Joaquín Díaz** 12:07 Can you document any of the steps that you take?
When you do the migration.
**Daniel Dyla (Dynatrace)** 12:13 No, of course. Because we don't… I mean, it's something that we've done, like, 3 times in 6 years, so…
**Joaquín Díaz** 12:20 Documenting it is…
**Daniel Dyla (Dynatrace)** 12:21 Yeah, I don't know.
**Joaquín Díaz** 12:28 So, yeah, I guess, yeah, we can at least… If we have, like, a list of steps, we can check with you that we are not missing something, if you are ready, we can do something right now.
**Daniel Dyla (Dynatrace)** 12:44 Yeah, I mean, the… a list of steps is fairly simple. In my mind, you just… close all of the open PRs with… I… With a… a message that says, please reopen in this repo?
**Joaquín Díaz** 12:59 And then…
**Daniel Dyla (Dynatrace)** 13:00 move all the packages and call it a day. And then Mark and the other maintainers and me and whoever when we see browser package PRs, We would just… Close them, and say, you know, this isn't the place for that.
**Joaquín Díaz** 13:17 Okay, but in terms of publishing the PRs, the packages, then you have to do something like… poignant.
to the same place on the new repo, on NPM. Some people don't know how to change that.
**Daniel Dyla (Dynatrace)** 13:30 It's certainly gonna be a little bit different, yeah.
**Joaquín Díaz** 13:36 Yeah, yeah, moving code is just moving code. Yeah, mostly worried about publishing and versioning when we start moving those.
Next.
**Daniel Dyla (Dynatrace)** 13:45 At least for the instrumentations, they should be… the publishing should be fairly simple, because the versions are not locked to the SDK.
So, you just change the repo field in your package JSONs and publish them as normal?
The secrets are stored, I believe, in the org, but they… I don't think they're stored repo-specific, Mark, is that right?
**Marc Pichler (Dynatrace)** 14:09 There's, no secrets anymore. It's, our YDC, Trusted Publishing.
So, the… I guess the step with the most friction would be setting up new packages. Since that has to be done manually, you can just publish new packages via OIDC, you have to publish them manually from your machine.
the first time, then set up OADC, in the… NPM UI, and then you can start publishing away.
So we'll need to figure out the process to, create new packages once they're ready.
To be published the first time.
**Joaquín Díaz** 14:56 Okay, can we choose one package that we know we have to move, and start there, and start seeing, like, what are the steps that we need help from someone else on, right? Where we are missing?
**Daniel Dyla (Dynatrace)** 15:08 Yeah, the packages that are in contribib should be fairly simple and straightforward. The ones in… the SDK repo are quite a bit different, because if we want version locking, then there would be some, Probably some friction there.
**Joaquín Díaz** 15:26 And do you think we should keep the same versioning that you use on the JS repo?
**Daniel Dyla (Dynatrace)** 15:33 Yes. I mean, I said my piece on this a long time ago.
**Joaquín Díaz** 15:38 Yeah.
**Daniel Dyla (Dynatrace)** 15:38 raised my hand and said, I don't think it's a good idea to have a separate repo. But… I don't have a good solution for version locking between repos.
**Joaquín Díaz** 15:54 With virtual login, you mean… the dependencies at that instrumentation, for example, if you need a specific API version and stuff like that, right? Not the specific version of the package that is being published.
**Daniel Dyla (Dynatrace)** 16:07 So, instrumentations should just have, like, a minimum API version. Like, that works with any API version 1.4 or later, right? Yeah. And less than 2.
The SDKs are different because there's a lot of, like.
Fairly tight coupling and interdependency between, Like, the, you know, for example, the trace package and the exporters and stuff like that.
And it's very difficult to mix and match.
all of those versions.
It can be done if you know what you're doing, but I mean, there's probably… A small handful, maybe less than 10 people, who really know everything that would be needed in order to make it work.
**Joaquín Díaz** 16:55 Yeah.
**Marc Pichler (Dynatrace)** 16:57 for stable packages nowadays, it's a bit easier, but that… you're still limited by the specification on that. The specification explicitly states that SDK packages need to be versioned together. So, Even if there's no technical reason, there would still be the specification that needs to be changed for that.
So you might want to look into that, if you want to decouple the versions there. And then also.
Re-exporting interfaces can… Make things a bit more difficult for you if you re-export, for example, the export interface.
Then somebody would write a exporter that's just compatible with web, which might be what you want.
But it might cause some confusion there. So there's different layers of this, where there's problems that.
**Joaquín Díaz** 17:55 People have not figured out how to surf yet.
**Marc Pichler (Dynatrace)** 17:58 Maybe.
Which might be more difficult.
**Joaquín Díaz** 18:04 Yeah, so let's say, for example, I want some… we want some more… This package from Contrail.
So, that package, I think… Like, the only dependencies are… the APIs… oh, it just uses the SDK.
**Daniel Dyla (Dynatrace)** 18:27 Instrumentations should only depend on the API. Some of the browser ones depend on… some SDK components, because they were written a long time ago.
a particular… Person.
But they should, if you look at all of the other instrumentations, they should depend on only the API.
**Marc Pichler (Dynatrace)** 18:49 Yeah, and the instrumentation pace, or the instrumentation interface, I guess.
**Joaquín Díaz** 18:54 Yes.
Yeah, that makes sense. So, right now, this package version is, zero… 0.53, 0.0, right?
So do you think, like, once we move this specific package on the browser repo, now depending on the API, if we can?
Then, we should keep the same version, or we should… should think about.
figure out, like, 1.0 or whatever.
**Marc Pichler (Dynatrace)** 19:24 So, since this is an instrumentation package, you're free to version it however you want.
**Joaquín Díaz** 19:32 Okay.
**Marc Pichler (Dynatrace)** 19:32 That's… that's essentially what the spec says, is, country packages, you… you basically can do whatever you want, right?
But for, let's say, SDK TraceWeb, it would be required to be versioned together with the core repo, as it is in the spec right now.
**Daniel Dyla (Dynatrace)** 19:53 the instrumentation.
**Marc Pichler (Dynatrace)** 19:54 and… Yeah, sorry, go ahead.
**Daniel Dyla (Dynatrace)** 19:56 The instrumentations are not considered to be a part of the SDK.
**Joaquín Díaz** 20:01 Okay, I think at first we want to focus on instrumentation and not the SDKs, so… Yes, so then no version logic.
**Daniel Dyla (Dynatrace)** 20:09 is…
**Joaquín Díaz** 20:10 Yeah, for the instrumentations, it's easy. No version locking is required.
**Daniel Dyla (Dynatrace)** 20:14 No, like, coordinated releases are required, really. When the SDK updates.
not the SDK. When the API updates, you would need to update, you know, your… but even… even at that, you might not have to, because you should be specifying a minimum API version. I guess only if the instrumentation package updates. Again, it's much easier to do, I guess is what I'm saying.
**Joaquín Díaz** 20:38 Yeah.
Okay, I think… I think we should start there, see how that goes, once we… move all the instrumentation to the browser repo. We can have another conversation about the rest.
Because otherwise, it's going to be a huge conversation that is not going to end anywhere.
**Daniel Dyla (Dynatrace)** 20:56 Yeah, I guess in order of difficulty, you have the… the contrib instrumentations are the easiest packages to move.
The SDK components would probably be, like, harder, and if you wanted your own web API, that's where you're… you're edging into very hard slash potentially impossible territory, if you want any sort of compatibility.
**Joaquín Díaz** 21:20 Myth.
Okay.
**Martin Kuba** 21:36 Alright, we have, just 10 more minutes or so. Joaquin, you had the next topic.
**Joaquín Díaz** 21:43 Yeah, so I have a PR that is almost ready to go, on the browser repo.
That is still up in discussion on the semantic commercial version repo about this. I don't know if you… Well, given that we are not publishing anything yet, maybe we are not… we are a special case, but do you usually First, try to match the semantic conventions, or you… Merge instrumentation, and then change it once the semantic conversion is done.
mostly what I'm trying to do is… I'm trying to get called into the repo so we can set up the rest of the tuning that we need, like, for building and CI and everything.
It's really hard to set up, set that up without actual call there, so… I was wondering if I can move… sorry, I can merge.pr on instrumentation, and we can set up everything there that we need to publish. We don't… we won't publish until the semantical version is merged, that's fine.
But at least the code is there, so we can keep setting up things on the repo.
**Martin Kuba** 22:55 Yeah, I thought there was a way to, to mark a package, like, a development state, so that could be, like, merged, but not… not published. I don't recall exactly, like, what the mechanism was for that, but if there was one… I think, Mark, maybe you were explaining to me This to me once, once, but, like, there's a difference between experimental and development.
**Marc Pichler (Dynatrace)** 23:20 I think we've had packages before that were just, marked as private and didn't pop.
**Martin Kuba** 23:25 Fueled.
**Marc Pichler (Dynatrace)** 23:26 inflammation, yeah.
**Joaquín Díaz** 23:30 Yes, no worries. I mean, I think we want to set up building on CI first.
Like, testing and everything, so… Yes, Alex.
**Martin Kuba** 23:43 Joaquin, I have… I'm trying to get up to speed with this PR, with the semantic conventions, like, one, I think the main thing for me, like, in this… For the user actions. It's just, like, to, decide, like, on the name of the events, and the attributes, like, which ones are shared. I mean, I saw that you had discussion about this a little bit with… on the PR.
But I do wonder, like, if, like, folks, like… people have, like, strong opinions about this, like, having… like, multiple different events for… for every possible event, or, like, have… have some, like, grouping of events. Like, I think there could be, like… we had or… we had the, like, one… we had a semantic mentions PR in the past that was… it was, like, a general user action.
event, and then I also saw a suggestion that maybe we could go, like, with something like… like a mouse or a keyboard.
events that, like, groups a few, like, mouse-related events together, or keyboard-related events together. So, again, I don't know, like, if that's… I would just wonder, like, if we should, settle this discussion first before… before merging this.
**Joaquín Díaz** 25:04 Yep. So… when I opened the PR on the schematic conversion, repo, I followed the same initial idea that I was using her name was, that there was this generic user action event.
There was a suggestion about using just click.
I was starting with Qlik, and then having individual elements, and I think it makes sense, mostly because When you have attributes, and you get an event that is genetic, for example, user action, and you don't know which attributes you will get, because it depends on the name, like, depends on what you are… Sending, like, keyboard, scroll, resize, whatever, you will get different attributes for the same event.
So I felt like it was harder to then… like, do something with that, if you don't know which are the attributes. If you have specific events.
You know, for sure, like, which are… which attributes are required, which are not, so you know what to expect.
On that object.
So that is why I think it makes sense. I still use, like, a user action namespace, so the name is browser.useraction.click.
In the future, we may have browser that uses reaction. Whatever else.
And, if we feel like there are common attributes between Things on the user action, then maybe we can think about how we can share those.
But I… initially, I like the idea of being very specific on what the attributes are, and to me, it makes more sense.
**Martin Kuba** 26:40 Okay, I also wanted to consider, like, from a back-end, back-end processing perspective, like, clearing… If, like, the use cases are more important to query, like, all different user actions, as opposed to, like, being able to query just, like, one type of user action.
Things like that, so… And I also don'.
**Joaquín Díaz** 27:01 Yeah.
**Martin Kuba** 27:01 I don't… I haven't actually looked at… the different types of attributes, like, if… I don't have a good sense of, like, what the overlap really is, or if there's an overlap, like, how much attributes are different.
**Joaquín Díaz** 27:15 Yeah, yeah, I haven't digged deeper, but for example, like, a very basic example would be, like, clicks have… they have, a correlate XY, And then, keyboards for typing on the keyboard, you don't have that, you have a key that you type.
So, those are examples of different attributes that you'll get on different events.
very basic, I haven't dig deeper on what else you can get on different events.
In that sense of, like, querying all the user actions, I don't know if all of you.
mainly to… Like, write your query in a way that you are looking for different events, like, using ORs.
Or… but yeah, you have to chase a grave, and you know, I think… mostly, I think it's… You still think that it's easier for querying for something that you know what you're expecting versus, bug of attributes that may change depending on what are the… the event that you're, meeting.
There's still a pending question about that anyways, around using the app widget click.
Event that already exists.
I added a question on the, SIG, on the client SIG repo. Sorry, Slack.
to get their opinion there, so I'm still waiting on that. If you also want to chime in, feel free to do so. Yeah.
Terrific.
we can continue the conversation either there or in the PR.
**Martin Kuba** 28:50 That sounds good, yeah, I'll comment there.
We've got, like, one minute left. Wolfgang, did you want?
Jaceric.
**Wolfgang Therrien** 29:00 Yep, nope, thank you, much for, the approval, Mark. I think, Martin, I think there's still a lingering request changes on that PR, so maybe if, you can give me a thumbs up on that. I know that I need to re-up the package lock, but hopefully we can get that, Get that cleared up this week, and get that instrumentation in. On to the next one.
**Martin Kuba** 29:22 Yeah, I'll take a look at it today.
**Wolfgang Therrien** 29:24 Appreciate it. Thank you.
**Martin Kuba** 29:27 And Jared, I don't know how much time you need.
**Jared Freeze (embrace)** 29:31 There's a link. I just wanted to document it. It's also in Slack, so check it out. It is a first pass. I'm not super happy… not super happy, but, like, the generator's not perfect, but just wanted to get it out there.
Does it…
**Martin Kuba** 29:50 Great.
Red time, I think, so… Thanks, everyone.
**Jared Freeze (embrace)** 29:55 Dear.
**Joaquín Díaz** 29:56 Thanks, folks.
