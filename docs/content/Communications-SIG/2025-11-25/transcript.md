SIG: Communications SIG
Date: 2025-11-25
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Vitor Vasconcellos** 00:53 Hello?
**Patrice CNCF** 00:55 Hello, hello?
**Vitor Vasconcellos** 00:58 learning.
**Patrice CNCF** 01:02 Good, how are you?
**Vitor Vasconcellos** 01:04 I'm growing, man.
**Patrice CNCF** 01:07 Meeting is being transcribed.
**Marylia Gutierrez** 01:12 So…
**Patrice CNCF** 01:14 Hi.
**Vitor Vasconcellos** 01:15 Hello.
**Leandro Caracciolo** 01:22 Hello.
**Patrice CNCF** 01:24 Hi, welcome.
**Leandro Caracciolo** 01:26 Thanks.
**Patrice CNCF** 01:29 Do we know if Severin is joining? Oh, there we go.
**Severin Neumann** 01:43 Hello, hello, hello?
**Tiffany Hrabusa** 01:45 Aye.
**Patrice CNCF** 01:46 Right?
**Severin Neumann** 01:50 Didn't you start without me, or what's, like, what's everybody waiting for?
**Patrice CNCF** 01:54 Yep.
We started the party? No. We were waiting for you. Just 30 seconds ago, was saying, when is Severn arriving?
**Severin Neumann** 02:03 I said, you were also not, like, bad-mouthing me, and you're laughing.
**Patrice CNCF** 02:07 Of course not.
**Severin Neumann** 02:08 But they were like, oh, let's stop that, like, he's joining now.
**Patrice CNCF** 02:11 We would have nothing bad to say, Severin, nothing. I hope so.
**Severin Neumann** 02:18 I hope so.
If not, I will watch the recording, and then, like…
**Marylia Gutierrez** 02:24 I was gonna say, like, as soon as we're done, he's gonna watch the recording, like, ha!
**Severin Neumann** 02:31 Delete recording. Anyways, awesome! Yeah, let me… then, since everybody was waiting for me, let me share my screen, and then I think we can get started. Can you see that?
**Patrice CNCF** 02:47 Yes.
**Vitor Vasconcellos** 02:48 Yes.
**Patrice CNCF** 02:49 Can you make it a bit narrower?
**Severin Neumann** 02:51 Just give me a second.
Yeah, I think, Leandro, since you're here today, maybe we can also, like, like I was not sure, like, talk about the… What's the best name for that? Like, graphics, visualizations, all of that?
But this is a second topic, if you're fine with that.
**Leandro Caracciolo** 03:23 I think the better way to talk about it is assets. Assets for social media, no?
So, first of all, nice to see you all, thanks for inviting me. My name is Leonardo, I'm working with FutureSC on Holy Garden.
So, first time here on the, on the, on the… the community.
Cult, so…
**Severin Neumann** 03:45 Awesome.
Welcome. And thank you so far for, like, already contributing some really good visualizations. I mean, some of them… those of you who have saw it, I mean, we used it for… to… remote hotel unplugged.
That was already, like, a good starting point.
So yeah, so… Hey Lucas, nice to have you here as well today. But yeah.
Let's maybe dive into the agenda. By the way, if you have anything you want to add to the agenda, I say, like, open up the document here. Also, feel free to add yourself to the attendees.
And… yeah.
If there's anything else, you can also use the chat.
Awesome, I think, Vitor, you had, like, the first topic, so maybe let's dive into that first.
**Vitor Vasconcellos** 04:38 Great. I was just wondering if we… we talked about this in the past meetings and, regarding the activity review, but I think we didn't mention the… The locales, the members.
**Severin Neumann** 04:56 Smooth.
**Vitor Vasconcellos** 04:56 The approver, then… So, I was just wondering if we… have some… process for this already, or if we should consider creating something. And I think there's also the… the workflow, Marilla mentioned.
I had it somewhere in my bookmarks.
That is…
**Marylia Gutierrez** 05:24 I can't find it again.
**Vitor Vasconcellos** 05:27 I have it. Wow, thanks.
**Severin Neumann** 05:33 And… yeah, that's it. Go ahead.
Right.
I mean, yeah, I mean, if we can get that workflow to run, I think that's… That's the best option that we have.
I think the only thing, like… Which is… I'm just thinking out loud, like, do we have… and, like, like, technically with sitcoms, We might have people… They are contributing a lot.
But they're not, like, directly adding anything to the repository.
Technically, But so far, we have not made any of those people triagers or approvers, right?
So if we think about Lisa, who is doing the hotel YouTube videos, right? She's adding a lot of value.
But technically, she's not an approver, but… or triager, but if we ever would decide, like, hey, that's a role she should fill, I mean, she also does a lot of that from a SIG end-user perspective and everything, but just picking on that. I think that's the only thing, but then I would assume that with the workflow, we could still say, like, hey.
just rejected PR or something like that.
for the localizations, I mean, then we would need to…
**Marylia Gutierrez** 07:06 Yeah, because this PR, I can say that it's just, like, any activity counts. So this one is, like, every four months, if there's, like, zero activity, is when it creates the PR. So you can say which groups are on this, so we can, for example, just add the list of, like, localization, not everybody. And, for example, the case for Lisa, she… Does… doesn't do, like, codes, but every time that she's actually doing her things, like, I'm gonna create a YouTube, she always creates issues for those. Okay, yeah. So that counts as an activity, so she would not get flagged as inactive.
**Severin Neumann** 07:43 Yeah. Patrice, you raised your hand.
**Patrice CNCF** 07:51 I'm trying to understand the broader context. Is there… or what is the problem that is trying to… is in need to be solved?
**Severin Neumann** 08:01 I think the idea was that, like, since we have… maintainers, approvers.
And at some point, they get inactive, right?
let's say I get inactive in 3 months from now because, I don't know, I do something very different, stop doing anything in OpenTelemetry.
very often, other maintainers feel not very comfortable to say, like, oh, let's raise a PR and.
**Patrice CNCF** 08:27 Got it.
**Severin Neumann** 08:27 moved from the repository, and then JS Sig solved it by having a bot doing that, right? And saying, like.
**Patrice CNCF** 08:35 First class not been active for 4 months, or something like that.
**Severin Neumann** 08:39 here's a PR, and they can comment on that themselves, and say, like, oh, I have been, like, I will be back, I was, like, on a parent leave, or whatever, or it's just, like, sure, we move them into emergency status, and then if they ever come back, we can consider, like, moving them back. I think that's… that's what this is trying to solve.
**Patrice CNCF** 08:59 So, just to be clear, the emeritus status is… essentially, the true effect is to have Certain identified users removed from, official org teams, is that correct?
**Severin Neumann** 09:16 Yeah, yeah, yeah.
**Patrice CNCF** 09:19 Okay.
And this, when there is a polling of activity, is it done across the org, or only within comms.
Do we know?
**Marylia Gutierrez** 09:35 No, so this is just, for example, opening a PR, saying, like, hey, this person is inactive, so you would remove that person from, like, the… if they are, like, I don't know, an approver on the communications, you still have to manually go there and remove them.
**Patrice CNCF** 09:51 Yep.
**Marylia Gutierrez** 09:51 This is just, like, to remove that awkward thing of, like, hey, I'm gonna remove you. Understood. Yeah.
**Patrice CNCF** 09:57 So my question was more about when the… in this script, when it… collects data about activity. Does it collect activity across the entire organization and all of the repos, or only, if we're doing this for comms, only in the OpenTelemetry.io repo?
**Marylia Gutierrez** 10:16 would be only on DA.io. Yeah, even, like, the page that you're seeing here, I think has, like, the repo… Name and stuff like that that you would update for this one.
**Patrice CNCF** 10:33 Coming back to Lisa's case, if the script were to… the entire organization in terms of getting… gathering data for activity, then she'd be okay. Whereas, if it were to only pull Hotel.io, then we might have an issue. So, I'm not… I think this is a good idea. I'm just Bringing up, potential issues.
**Severin Neumann** 11:04 Tiffany.
**Tiffany Hrabusa** 11:07 I also think it's a good idea, but I'm… I'm curious what we plan to do about the vacuum that this might result in, if… For example, some of the locales, we've seen a drop-off in activity from the approvers, but we see other people still contributing PRs.
it doesn't exactly change the situation, but if we remove the approvers altogether, then there's nobody who could potentially review those PRs that are piling up, so… I'm just wondering if maybe there should be another action step associated with ra- with the bot… raising this PR is that… we do some kind of outreach to these people, like, maybe.
**Marylia Gutierrez** 11:53 Yeah, so the idea that we created this onto JavaScript is because, like, you look at the list of approvers, oh, we have five, we are good.
So, we are assuming we have 5 people reviewing, and then this one actually checks, it's like, oh, none of those 5 have been active for more than 4 months. So, in reality, we don't have any approvers, but if we look at the list of approvers, we are always like, oh, we are good, we have it. So, this is more like.
If we remove, like, when you open the PR, the person will get tagged, so it's a chance for them, like, hey, you still want to be active? Like.
Or are we gonna remove? And if we remove, we realize, oh, we don't actually have any extra active ones, so we should maybe see the person who have been helping out, and move them to approver. So it's more like a reality of what is actually happening.
**Tiffany Hrabusa** 12:42 Okay, yeah, as long as the person subject to removal is contacted in some way, and, like, we're trying to have that conversation openly, like…
**Marylia Gutierrez** 12:51 Yeah, it's not like… it's not like a.
**Tiffany Hrabusa** 12:53 Defaulting.
**Marylia Gutierrez** 12:54 Yeah, it's not like something that automatically creates the PR and removes them. This is more like, creates the PR, tag the maintainers, and tag the person, saying, like, hey, we're gonna move you, and then they got a chance to, like, reply and stuff like that.
**Tiffany Hrabusa** 13:08 Okay, sounds good.
**Severin Neumann** 13:10 I think it forces us to think about that from time to time, right? I mean.
We definitely could better… do better, like, reaching out to people that are contributing. So the moment we get a PR that says, like, hey, remove some people, we maybe also think about more, like, adding people.
So yeah, and… Maybe… One more comment, I think… we should keep it only on the Opentelemetry.io repository, because, I mean, we had the situation where we had people that just moved within the project, right? That said, like, hey, I contribute more in this and that language, but less on docs, and I think that's worthwhile still to say, like, okay, let's demoed them within docs, because, like, they just moved into another project. My final comment on that is, like.
let's run with it, and if we don't like it, then let's remove it once again, right? I mean, this is not something we… we're tied to use, so… so Vitor, if you want to run with that and provide a PR.
**Patrice CNCF** 14:15 Yep. And…
**Severin Neumann** 14:16 work with Marilia on, like, making it work in the .io repository.
then, yeah, I would be more than happy to have that.
**Vitor Vasconcellos** 14:26 Alright, we'll create the PR and… I'll scary. I grew up.
**Severin Neumann** 14:33 Awesome.
Oh, let me actually.
**Patrice CNCF** 14:42 Whoa, this is one of our best attended meetings in.
**Severin Neumann** 14:45 What?
**Patrice CNCF** 14:46 Welcome, everybody! Good to see everybody.
**Severin Neumann** 14:50 I don't remember us having 10 people on a comms meeting in a while.
**Patrice CNCF** 14:54 Yeah.
**Severin Neumann** 14:58 Wonderful. Yeah, wonderful.
Ryan, let's dive into the next topic, as I said, since Leandro is here and I asked… him to… to join us today. So, just to add context for those who don't know, so Leandro is working with Ollie Garden, right, and he's… he's a designer, and he already created some really good visualizations, actually two of them. One is, like.
This social media support for… our hotel unplugged, and the other one is, like, a set of, let's say, generic images that we can use on slides, or social media outreach, and all those things. I can actually Maybe quickly find… Tim.
PR that contains them, because I think it's also good.
For people to see them.
Let me see… Here's… oh, no, let's use the big one.
So here's, like, right, so those are, like, images we… We could use for… Social media outreach for… whatever we think about, right? And, And, like, that's one topic, and there's another topic we can talk about this later. And I think there's, like.
there's, like, two questions we need to answer for that. One I think we have answered already is, like.
Make it accessible to people that are not designers, or not people that are, like, really good in doing, like, any image editing.
And I think the really cool thing is here, like, yeah, I can just go here in the Google Slides and say, like, oh, actually, like, let me make a copy of that, and then, like, I don't know, change the text, or he'll, like, change the image of that person and put whoever is doing the talking here, etc, etc, right? I think that's solved.
The other part is more around, like.
and this is more a generic issue, we had this question, I think, before, is like, how can we make, like, that accessible then to designers in general? Because, sure, it's awesome to have you on board, Leandro, but the moment another designer shows up.
how can those people then maybe also make edits on those images, or collaborate on that? Which is very different to how we do it with code today, right? I mean, with code, we just put it into a repository and people can collaborate. I'm not sure what a good practice is for visuals, right? Like, is there, like.
some, some, some, some tooling for that, that, that, that we can use. Patrice?
**Patrice CNCF** 17:45 Great work. Thank you for sharing that, indeed.
Much appreciated.
Given the files in what format, whatever format they end up in, if it's different from this.
If we can start using the shared resource folder, and that could be a way to make it accessible broadly.
I think I'd propose that in the issue. I don't know what you feel about that. We might want to have… I don't know, originals that might be locked, and or only view accessible, and then Another part of the folder with other resources where people can make changes and submit submit changes, Images they might create.
And they could be reusable. So those are my initial thoughts.
**Leandro Caracciolo** 18:49 Well… Originally, I created that on Figma, no, because it's easy for me to create, and for another designer, I think it's a good… It's a good software to use.
But this is not open source, so I don't know how the community works with that, no? Someone created this suggestion to rebuild this on the Google Slides, you know, fix a better option to anyone to use it, to anyone who's not a designer to use it.
I think Canva is another possibility, too, to… we can create a custom Canvas and work… on this, and I think the designers use it, and designers use it too, no? So it's a possibility. I can create the versions on SVG, for example.
And put it on the drive, and…
**Patrice CNCF** 19:38 Isn't there an open source, equivalent of Figma that came out recently?
So just… just a comment about Figma. In the past, we've had, OTEL resources created in Figma, and eventually we just… we lost access to the files.
So, it may… Great tool, and nice environment to work in.
But if we can't guarantee that we maintain access, maybe we can, maybe there is a way to do so, but I think that's one of the main… Concerns.
**Leandro Caracciolo** 20:17 I think we have another option.
that do the same as FILMA. I have to… I have to, to, to… search one of them, but I think it's a 6, no?
**Patrice CNCF** 20:30 So, sorry, Sofa?
Fabrizio just pen pot? I don't know if it's pen pot. I just…
**Fabrizio Ferri Benedetti** 20:37 I saw it in…
**Leandro Caracciolo** 20:38 Penpot, Penport.
**Patrice CNCF** 20:40 Okay.
**Fabrizio Ferri Benedetti** 20:40 It seems quite feature-complete. Worth a try, I would say.
**Severin Neumann** 20:47 And you say this is open source, so…
**Fabrizio Ferri Benedetti** 20:50 Yeah, it's… you can self-host it.
and I guess they offered the, yeah, the cloud version is probably paying, and… Then you can install it, Yeah.
Well, in that case, we would need a bit of infrastructure, but… yeah.
Which I don't know if the CF provides.
**Patrice CNCF** 21:21 have to look into that. Coming back to Figma, is there a way that we can I don't know if it works like Google Drive, where you can just share permissioned access? Is that possible with Figma?
**Leandro Caracciolo** 21:36 Can… I can export it, for example, the final SVG, or…
**Patrice CNCF** 21:42 No, but actually the original, the main Figma file itself. Faberi, you're saying yes, that's fine?
**Fabrizio Ferri Benedetti** 21:48 Yeah, yeah, yeah, I mean… Well, I mean, you can create a free account, and I think you can share the… the workspace, right, with any user.
So… at least in our… in our Figma instance, we can do that. We can, Are you using Figma or Figma Jam? Because they're also slightly different.
**Leandro Caracciolo** 22:09 Figma.
**Fabrizio Ferri Benedetti** 22:10 Figma.
**Leandro Caracciolo** 22:11 Pigmented other designs.
**Fabrizio Ferri Benedetti** 22:12 So it, it does have, it does have share… share files, share support, but, yeah.
**Leandro Caracciolo** 22:19 It's limited.
**Fabrizio Ferri Benedetti** 22:21 Yeah.
like, of course, you have to be inside Sigma, and have a user seat, and all that, yeah.
**Severin Neumann** 22:33 Just to summarize, I think… I think we have, like, three problems that we need to solve, right? One is, like, making it accessible to non-designers, and I think we fixed that one, at least partially. Then making it accessible to designers, we're debating that, and the third one I hear is, like.
Let's say, how can we ensure that we own the resources forever, right? Like, especially, Patrice, the example you gave, like, we create something in Figma, and for whatever reasons, we lose access to that platform.
how do we… how do we ensure that, right? So, so I think… part of that is, like, finding the right tool, so is it PenPod, is it Figma? I think Kanva, for example, and this is maybe something more than on the CNCF level, like, they have a… For non-profit version of it, like, you can apply for having a non-profit license, but that's probably then also, like, for a year or something like that.
But the other thing is definitely, like, yeah, we should ensure that, like, every time such a visualization is created, that, like, an SVG or whatever kind of file is put… on a Google Drive. So the last part, I think, is more around a process, right? That we say, like, hey, every time you, Leandro, or anybody else is, like, contributing some visuals, let's make sure we have… like, something that people can work off. I'm not even sure if an SVG is… the best version for that, I don't think so, like, PSDs or whatever, is then editable, and any tool is maybe better. But yeah, I think that's, like, the problems that we need to address, and if we can do that, I… I'm… I'm very eager to… to change a lot of visuals on our website, right? Because, like, if you… if you look at, like, just… just to give you a very… Recent example, I updated the context propagation page, and I added that visual here, right, I used… XCalidraw for that, I mean, the advantage is there, like, it's kind of open source as well. It looks okay-ish, but it's not, like, polished, right? And if we can, like, get polished versions of that, but at the same time something that can be easily edited, I think that's… That, that's, that's then perfect.
Patrice?
**Patrice CNCF** 25:07 I, thanks for the summary. I agree with what you say. Also, just wanted to emphasize that even though SVG is editable, we've had headaches in the past of it not.
pretty much being too encoded, so having access to the original documents from which the SVG was generated would be way better.
And a question, did you say that the CNCF already has some sort of…
**Severin Neumann** 25:33 No, I was wondering if they have one already, like…
**Patrice CNCF** 25:36 Okay. I… I… I can inquire.
**Severin Neumann** 25:44 Yeah, but, but I, I think to… to make a very long story short, I think, like, using Figma is fine, like, Leandro, if this is, for example, like, the place that you prefer using.
But then, like, what we need is, like, that kind of exports where we say, like, hey, we can make it… make edits even without, like, every time, like, getting back and forth to you, right? Like, And then the other thing is, like, how can we, like, put it on a Google Drive or something like that at the moment?
I say you say, like, hey, I'm no longer contributing here, or Figma is deciding to pull access, or whatever, that we are on a safe side, right?
**Leandro Caracciolo** 26:29 Well, Figma… Figma is my preference, but I can work in another software if you think… what's better for the community, you know? Not necessarily could be on Figma. If you choose, for example, no, let's use Illustrator. Okay, so I'll repeat this on Illustrator, and…
**Severin Neumann** 26:46 Okay.
**Leandro Caracciolo** 26:46 I'm able to change it for what's the best for the community.
**Severin Neumann** 26:52 Okay, I don't think we have an immediate answer for that, but I think we should figure it out over the next… Few days and weeks.
I think for the time being, use Figma for that, and then we see, like.
Because, like, just to emphasize that, right, this is not a new problem that we have, right? We had designers trying to help us, we captured some of the value that they created, but as Patrice said, like, for some of the visuals, we… we then lost, like, the possibility to… to update them ourselves easily, because we only had an SVG, but this SVG was not… like, the text was not rendered as text, for example, and things like that. And that's why we're a little bit… how do you say, like, defensive on this topic, but if we can figure that out together, and that's why I think it's good to have you here today, then I think, like, there's a lot of places where the OpenTelemetry website Could profit from some… better visuals, or new visuals, right? I mean… We, for example, we never updated the landing page. So if you ever want to take on a really big challenge, that's definitely also one we could do anytime, so… But yeah, anyways, I think there's a little bit of homework here, and again, highly much appreciated your help and your support here.
And for everybody else, I encourage you to… Think about places where we need designs and visuals and everything, since we now have someone who's eager to help with that.
Awesome. Anything else on… On that topic.
No, does not look like it.
Then let's maybe… Talk about the triage process for a little bit.
Let me bring it up, just give me a second.
Yeah.
So, so maintainers know this already, but I wanted to share this with, with everyone, and also spend some time on discussing that, like.
What we never had, like, on the .io repository is a proper, like, triage process.
And I just took… like what we have already, like, not documented, I mean, we… do some triage to some certain extent. And then I took, like, a few practices from other repositories, and just turned it into, like, process that looks very complicated, but actually is not. So the idea is that, like, if you look at an issue, then take a look and say, like, hey, is this something for, like.
a SIG, so it's just, like, co-owned by, like, collectors, C++.
operator whatever, or is this a localization thing, or is this, like, something that's, like, doc-specific? Which is, like, a catch-all thing, right? I mean, there's places I would even say, like, yeah, we might need someone. And then, like, the other thing is, like, okay, is this, like.
Just accept it, or do we need still to decide on that? Or can we just reject it because it's like a duplicate or something like that?
And then it's also helpful if we, if we type it, so, so, GitHub now has types, which are bugs and enhancements.
But, like, also there's, like, questions and copy edits, and I said I just mapped a bunch of things that we have already on that.
So yeah, that's… that's, like, the idea with issues. I also wrote a little bit about PRs, but I wanted just to… to… to get some feedback on that, or if anybody has tried it maybe already, so I played around with it recently, and I found it doable. But yeah.
Let me know.
solved comments.
**Fabrizio Ferri Benedetti** 31:06 Sorry, one thing, I recall we, we had… we were trying to use the project board for, statuses. Like, does this tie to that attempt of… of using the project board? Like, is this something that the triagers could help?
also curate.
**Severin Neumann** 31:24 Actually, like, I have not even thought about project boards, but of course we can make this happen as well, right?
**Fabrizio Ferri Benedetti** 31:30 Unless we want to drop it, of course, but, you know.
**Severin Neumann** 31:33 And my thing is, like.
But as, like, a personal preference. I never ever work off project boards on GitHub.
**Fabrizio Ferri Benedetti** 31:42 Yeah, same, same here.
**Severin Neumann** 31:43 they… so my workflow is normally that I get… go into GitHub notifications and just do, like, a… very broad triage, but the thing I also found very helpful on the… on the spec repository, is that, like, that you have, like, a quick way of just to throw everything out that is triaged already, and then see, like, okay, there's another 300-something issues that just need triage, maybe just need to look like… is this accepted? Is this something we need to debate, or is this just something we can throw out? Because, like, I did this last week, and I think I found a bunch of things we had open forever, but they were completed already, right? Or… I just said, like, hey, we actually don't do that.
I don't know how anybody else thinks about project boards, but every time… I try to use them a few times, and, like, every time I do, I'm just not… feeling compelled.
Using them, but anyways, that's… that's just, as you said, like, a personal preference, so… .
**Patrice CNCF** 32:49 Same.
**Fabrizio Ferri Benedetti** 32:52 Yeah, I think, I think our issue's view is already working as some sort of Kanban, in a way, with the labels and stuff, so… I'm using mainly that view.
**Tiffany Hrabusa** 33:07 I use project boards in my… Grafana life?
But I also have not found… The right configuration for a project board for, the hotel stuff. I'm using one right now for the collector docks refactoring.
mostly because I have to make that public for CNCF.
I have to have, like, some good way to track progress that we're actually making.
But I'm not relying on the project board to… yeah, I haven't set it up well enough. I think there maybe is a way to use a project board efficiently and, well, I just haven't found that… that configuration. Yeah, Marillia.
**Marylia Gutierrez** 33:55 Yeah, I was gonna say, like, I think really it varies a lot from the project. So, for example, on the JavaScript, there is one big project about, like, declarity config.
And it's mostly, like, me working on it, but I want people to start helping, but they don't know which part they can't help. So I did create a project for that, and it has the column of, like, all the tasks that need to be done, but they're not ready to pick up. Then I have a column, like, you can pick up any of those. And then I have, like, the in-progress and done, and now people are being able to just look at there and know when they're ready to pick up, because it's… It's such, like, a huge project, and it's hard to find which thing is ready to pick up.
But it varies a lot.
per project.
We don't do that on any of the other projects, all the JavaScript, just this one.
**Severin Neumann** 34:43 I think that's the point, like, a project board makes sense for a project, right? Because, like, having a board that has, like, 325 open issues, split across, like, that's not, like, helpful, right? But I think the collector… rework is a good example, right? And we should maybe think about more like that, like, hey, are there, like, projects? And Patrice, I think you also threw in, like, the idea of using milestones.
**Patrice CNCF** 35:10 Right.
**Severin Neumann** 35:11 Like, hey, are there things, like, that we… that we can… Group together into projects, and then work off them, and Marilia, I really like this idea to have, like, a column-like… hey, this is something blocked, because, like, we as maintainers are currently not able to help you with that, but there's a bunch of things, like, for this specific project, I don't know, like, collector… rework, or we… I still have this whole getting started project open, or… I think there's a few other ones that… that we maybe could… could come up with and say, like, hey, let's work off a board versus, versus the… that list, so… so, yeah.
That's actually a good…
**Fabrizio Ferri Benedetti** 35:54 I think localizations… localization teams could also probably benefit from setting up their own boards, and I guess they can right now. I don't know if they have the permissions to do so, but…
**Severin Neumann** 36:05 We have a support, right? We have a…
**Fabrizio Ferri Benedetti** 36:08 Do we have some?
**Severin Neumann** 36:10 Yeah, we have a centralized port for them, let me… Let me share that with you. I'm not sure if anybody's using that, but, like, I created, like, this board here, and they can, like, restrict it by language.
But apparently nobody's really using that.
Yeah.
**Fabrizio Ferri Benedetti** 36:34 Okay, but yeah, that's a good example, I think, because we… You know, it's quite convenient for anyone, trying to just filter out localization stuff.
**Severin Neumann** 36:44 Yeah.
**Fabrizio Ferri Benedetti** 36:45 to me, my thought around this is more… is kind of collateral to this, but it's more at the source, which is, I feel like we need to define more projects.
Because the… I don't use a project board because I… I don't have, like, many… big projects they collaborate to, right now, and I feel like I'm mostly being reactive these days.
So I think we, we mentioned sometimes, like, thinking about more, like, like a North Star strategy time, maybe coming up with objectives.
for… for the commsig, I think we… we need a bit more… I don't know, maybe with a, every six months cadence, I don't know, but… It's… Yeah, I think it… I'm aware of this problem more when I think about the project boards, but it's there, right? And .
**Severin Neumann** 37:45 No.
**Fabrizio Ferri Benedetti** 37:46 Yeah.
Now that you mentioned visuals, that could be a project we could… we could come up, you know, we could create the landing page is… is another landing pages, is another project, potentially.
You know, with something like this, then it's a matter of filling the gaps, creating the issues, tracking, defining milestones.
Yeah, I'm longing for something like that.
**Severin Neumann** 38:15 Patrice?
**Patrice CNCF** 38:16 So, totally agree, and… my suggestion to use milestones as a tool was in support of that. So essentially, it… if we were to do this once a month, I think is too much.
So every 6 months or every quarter makes sense to me, and… An incremental improvement over what we have now, which is… nothing much, but… So for one quarter, to choose the three top efforts that we would like to focus on, and be proactive in that. And I agree with you, rather than being in reactive mode, so be proactive to identify the top 3.
**Fabrizio Ferri Benedetti** 39:02 Yep.
**Patrice CNCF** 39:04 user experience improvements that we can do for comms, that would be great. And that's what the milestones were there for. It wasn't to… yeah, it was to give us that Vision of, for a quarter.
**Severin Neumann** 39:19 Yeah, yeah. Just, just to, to… support that, or say some… like, one of the reasons why I wanted to have this triage process is exactly that, like.
I recognized that, like, over the last, especially, 12 months, and there were, like, a variety of reasons, like, a lot of us moved jobs and had, like, other things, like, getting into their way of, of, like, contributing, but we were really, really reactive in the last year, right? Like, like, I… I did, like… not a lot of major docs changes myself, like the context propagation thing, like I wrote last week, and this took me, like, half a day, right? That's just something we have to remember, like, sitting down and writing proper doc… docs, even, like, with the help of a little bit of an AI, Is, is, is, like, a lot of work, but that's, like, at least for me.
the fun part of the work, right? Like, writing docs, and I want… us, or especially I want you, many of you being, like, technical writers who are excited about technical writing, spend more time on that versus, like.
going through that backlog and reviewing yet another blog post, and all the things that are just flooding in, right? So… and my goal for 2026 would be that, like, we find a new cadence and a new… new… Fresh energy for… focusing on dogs, right? Versus, like, just chasing everything.
and triage is hopefully that thing where we can say, like, hey, we accepted the thing, or we rejected. And I also want us to reject things with, like, not right now, right? This is a great idea, we should definitely do this someday. Like, we get a lot of great ideas of, like, hey, we should, I don't know.
reworked this whole operator documentation thingy here. And we can say, like, yeah, that's a great idea.
And then we can still say, like, we reject it as not right now, or we accept it and say, like, yeah, but… that's someone else's problem, right? I'm totally fine with that.
Hope that makes sense.
The other thing, like, that's missing is a little bit of automation, like, to bubble up some of the triage things again after a certain time, and say, like, hey, is this still relevant? Because that's something we are not doing, and we still have, like, a few hundred open…
**Fabrizio Ferri Benedetti** 41:44 Yep.
**Severin Neumann** 41:44 issues. But yeah, slowly and slowly, but… but I think the…
**Fabrizio Ferri Benedetti** 41:49 Can we, yeah, sorry, sir.
**Severin Neumann** 41:51 the big, big, big thing I just want to say is, like, make writing docs a priority, right?
If you, and maybe to add this as well, like, if we want to establish something like that, we can also talk about this.
Cates is doing that. They have, like, Like, a rotating… triager duty, right? So they say, like, hey, every maintainer has, like, one week per month.
where they are responsible for, like, doing the triage, for doing the reviews, and everybody else is freed of that, so to speak. I'm not sure if this is really something we want to do, but we can debate that. Anyways, Patrice?
**Patrice CNCF** 42:37 Might be worth scheduling… That in the early New Year to make sure we come back to it.
And maybe sit.
Set our priorities, establish maybe our first top three.
Proactive areas that, we would like to work on.
There was something else I wanted to mention, but…
**Fabrizio Ferri Benedetti** 43:03 Yeah, I agree with that, with that proposal, and at the same time, even as preparation, I was wondering if we could Find some mechanism, it can even just be a shared docs where we could, like a bucket.
Of project ideas, milestones ideas that we could… where we could collect Thoughts on, like, the big themes that we could be working on.
And I guess that… how many of you in the call are currently in the governance committee?
Sync… Is there… I don't know how it works, like, I don't… I don't know how it works in the internals, but is there any chance you could get, like, inputs from there on things that could become themes?
Or, like… Do you also get, like, a… do you get, like, strategic inputs from other areas that are developing within.
**Severin Neumann** 43:57 I mean… Yeah, I mean, one, one, one big, big, big, big theme, like, hopefully you saw that blog post around stabilization and…
**Fabrizio Ferri Benedetti** 44:06 Yeah.
**Severin Neumann** 44:06 I liked how Austin phrased it last week, making open telemetry more boring. I think that's, like.
the big agenda of OpenTelemetry for the next…
**Fabrizio Ferri Benedetti** 44:19 Like, one of the things I was wondering today, because we also got an update about stabilization, for example, is that the documentation for some of the main collector components, I believe, are still Redmi files, right? So… we don't have to meet the docs, or do we? And.
**Severin Neumann** 44:37 I think that that's something… Collector is very specific on that, right? Because, like.
**Fabrizio Ferri Benedetti** 44:41 Yeah.
**Severin Neumann** 44:42 We want to have all the docs for all the components in our repository.
**Fabrizio Ferri Benedetti** 44:46 Hmm.
**Severin Neumann** 44:49 Yeah, I don't know if this is a good idea.
**Fabrizio Ferri Benedetti** 44:51 But that's something, like, Tiffany is working with the collector's sake. Right, but, you know, just as an example of, you know, we have a big theme, and maybe we can spun, like, we can spin an idea, or…
**Severin Neumann** 45:03 Yeah. From the teams, yeah. Another thing I, I, I totally get, like, like, I think if I… if I would need to pick themes right now, and it's very, very biased right now, it's definitely the collector Documentation to get this Done.
the Getting Started project I launched almost 12 months ago, and just did not get up and running for, again, a variety of reasons.
And then our project, we should also be, like, aware that it's, like, tangential to our SIG, is this whole ecosystem explorer thing.
which kind of also… goes towards what you said about, like, the documentation of important collector components. How do we see them into what we are doing? That's maybe a little bit tangential, so that's why a third one I would like to choose is what I mentioned to you in a one-on-one conversation, I suppose.
is the whole concept pages, right? We really, really need… I said, all of them, and say, like, hey, are they still up to date, right? And do they need, like… I said, that's why… one of the reasons I tackled the context propagation.
because a lot of them are not in a really, really good state, right? So even if you, like, go into components.
Yeah, I think, for example, that a lot of people asked for is, like, a what to use when documentation, which is kind of the components documentation, to say, like, hey, when should I do manual instrumentation? Should I use this kind of automated instrumentation? And all this, like, this, this, this universe, so… so that's definitely something I see, see important.
Tiffany.
**Tiffany Hrabusa** 47:00 Just kind of a side note that if we have a lot of, projects in mind.
But we don't always have the manpower.
We could look into doing an LFX mentorship.
that is designed around a project, and bring in somebody to just focus on that one thing. It would require time on our part to do the mentoring, but it would mean that we might get to check something off of our list. Just a thought.
**Patrice CNCF** 47:38 Great idea.
something that I've… Wanted to bring in, eventually ended up doing it for other projects, but certainly something to consider, the mentorship.
There is a project coming, which is actually sponsored mentorship, that we'll be talking about.
soon will be discussed in the GC, and maybe we can talk about it here afterwards, but that would be different.
I remembered what I wanted to say before about the blogs. So, we do indeed put in a lot of effort.
in the blogs, and I think we're mindful of what goes in and the quality.
I don't know if you look… remember looking at the statistics that I shared earlier, and our blogs are not consulted that much.
And as I mentioned, one of the explanations might be that often they are cross-posts, and that we put as the canonical link the other The original.
So that might be an issue, but I just thought I'd bring it up that Early in the year, we might want to revisit our… strategy in terms of how much effort we put into the blogs. If they're not delivering that much to our community, to the community.
Yeah, that might be something to consider.
**Tiffany Hrabusa** 49:08 Yeah, I think, I agree with that. It has been a lot of work, and if there's not a lot of payoff, then, We should definitely reconsider that, but… I think as part of that discussion, we need to figure out how to… publicize what's going on with the project, then? If it's not through the blog, how are we going to keep people informed?
whether that's just purely social media, without the blog post attached to it, or if there's some other mechanism. Because I know From conversations with other contributors that that, like… advertising what the project as a whole, but also sub-projects are working on, and what their priorities are, is a big blocker to most people coming in as new contributors. Like, they don't know… where to go, which SIG, but once they get to the SIG, they don't really know where they can make the most impact, like, what the priorities are, and it's kind of opaque, so… that might be part of the discussion as well. Like, maybe we find a better way to highlight these things than blog posts, but I don't know. Don't have any, like… Real ideas about that.
**Patrice CNCF** 50:28 Just to be clear, so my suggestion was not necessarily to… fewer posts, at least internal posts, but maybe… More in terms of I guess external cross-posts and things like that, that we do end up spending time reviewing.
Which may be… Less productive use of our time for those external posts.
**Tiffany Hrabusa** 50:57 Okay, yeah.
**Patrice CNCF** 50:58 It could be… Yeah, as Severin was saying earlier, as triagers, we should feel free to reject things. Well, maybe… if we reconsider our priorities and how much people actually don't visit the blog posts, we should consider rejecting some external ones. I'm just trying to suggest maybe there's a potential for rebalance in terms of the efforts we.
**Fabrizio Ferri Benedetti** 51:20 Yeah.
Yeah. My impression… my impression is that this could happen organically. I mean, once we… get to a point where we have big projects, big priorities for writing new docs, etc. I feel like the space for other things will diminish eventually, once we prioritize. Right now, perhaps, we don't have that much prioritization pressure, but, you know, possibly next year we will.
**Tiffany Hrabusa** 51:50 Yeah, I… I think there's only… I mean, I'm trying to remember… maybe I've blacked it out, but, like, the last few months of blog posts, I think there's only been… Maybe one or two that were actually cross-posted.
from other sites over, like, the last slew of… of posts. Most of them were internal, and I get that October is a busy time, because there's KubeCon coming up, elections, awards, like, it's a busy time, so… Okay.
But… Yeah, I think… Maybe not rejecting outright, but we can, you know, we can… Be more forceful about our schedule, and say that we… we appreciate this post, but we will not be able to get it up for 2 months.
like, set the expectation that it's not gonna get posted anytime soon. That… that might be…
**Severin Neumann** 52:45 I think that that's what I also wanted to throw in, like, one… We should just… maybe that's something we should put there, like.
We do only that many blog posts per week, maybe one.
I, I think that's, like.
Then what… like, internal blog posts, yeah, they're slightly different, but, like, we have, like, a bunch of them that are just, like… I mean, think about the ones for the GC election, like, we just take the ones from last year, change the text, and put them up there, which is a lot less work than, like, hey, here's how you can use OpenTelemetry to monitor, whatever, is, is much more work.
And that's actually why we introduced this thing here a year ago, right? Where we said, like, hey, there needs to be a SIG sponsoring your blog post.
So I think one big piece is, like, we should be much more forceful about our own rules, because what I saw a few times happening in the last few months is that, like, someone put up a PR for a blog post, and we already started reviewing it before even following our own process, right? So if we are like, hey, there's a blog post, and they have not raised an issue, then we say, like.
yeah, this blog post… I mean, if you like, we automate that, right? And then have a bot tell them, like, yeah, if you don't have an issue, and if you don't have a sponsoring SIG, we are not going to review that thing. And sponsoring SIG, for me, also means, like, there is a person in that SIG that will come to us.
And read that blog post and tell us, like, yeah, that's… that's correct what that person is writing there, right? So, See you properly. So, yeah, I think we should just be more forceful about that, and then… Of course, full is a hard word, but… foreseeing our own rules, right? Patrice?
**Patrice CNCF** 54:43 Thanks, you're right.
just forgetting about the policies we have in place, just because there's so much going on. What I wanted to bring up is that, and this comes in part from the CNCF, there's encouragement for us to use AI tools, and I've been playing around a lot with that.
In particular with, for example, automated, well, AI-assisted upgrades for Doxy for projects, which is a pain to do manually, and it's great to get some help. But, all that to say that this definitely could be an area where we can at least get some assistance.
And, I've been working towards that, and I don't think I'll have time before the end of the year, but definitely setting up Well, here's my vision, and let me share it with all of you.
Febony and I had talked about this already. There's a slash site, subfolder under the… website, and it's meant to be for internal documents, essentially us describing how this site is built, etc.
I'd like for us, rather than writing AI-specific Markdown files and instructions that we write processes… document our processes so that they're consumable by us as maintainers and approvers and triagers, and that we can point AI assistants to, to say, run this process. That's what I've been doing on other projects. I've documented a process, and then I point the AI assistant to a particular subsection and say, okay, do this update.
And I think this could help a lot, because, OpenTelemetry is growing, our processes are growing.
And I know for me, it's easy to forget about the great documentation we have for the processes. So yeah, that's my vision, I guess, part of what I'd like to set… help set up in 2026.
for us.
**Severin Neumann** 56:56 Yeah, yeah. No, I think that that's definitely something we should… We should also, like… Look into… always with the idea in mind, like, how can we make our own lives easier, right?
We have 4 more minutes left, I have a hard cut. Maybe one last comment from my side on the whole triage process, which triggered off this variety of topics. Please try it out.
And, and give us feedback.
This is maybe especially, like, to the non-maintainers here on the call. If you want to help with triaging.
We technically would need to make you a triager, so that would mean, like, you need to be a member of the… at least a member of the OpenTelemetry project, so that means, like, you have to have a set of contributions already.
If you have that already, like, 4 or 5 contributions, then reach out, we can, like, work on the sponsorship for membership, and then I say, making people triage is, let's say, the easiest thing we can do.
If you want to help with that, right? Because I'm more than happy to have people, like, look into that, and if it's only, like, tagging tagging the right SIGs, right? Tagging, like, oh, this is collector sick, like, we… maybe there's also something we can give to a bot at some point, I don't know. But I would be worried that they don't get it right, so… Anyways… Anything else for the last 3 minutes? Anything we should have talked about, and… Need to push out for in 2 weeks.
**Patrice CNCF** 58:36 Whoever's taking notes, thank you very much. It's an anonymous Loris.
**Tiffany Hrabusa** 58:41 E.
**Patrice CNCF** 58:46 Thank you.
**Severin Neumann** 58:49 Awesome.
Nothing else.
I… am excited to have you all here, 10 people in one meeting. I think we're doing good. Now let's hope that we have… as many people are contributing to the repository next week. Anyways, I wish everybody a happy Thanksgiving, who's living in the US or celebrating Thanksgiving.
everybody else, two very calm days without meetings, that's at least what I expect for Thursday and Friday. So, yeah, talk to you in two weeks. Thank you, bye-bye.
**Patrice CNCF** 59:26 Hi, Happy Thanksgiving. Bye, everybody.
**Vitor Vasconcellos** 59:28 Bingo, bye.
**Leandro Caracciolo** 59:30 Right.
