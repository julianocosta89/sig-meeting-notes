SIG: Service and Deployment SemConv
Date: 2026-01-08
Duration: 36 minutes
Zoom Recording URL: https://zoom.us/rec/share/VvyXXg5mQJKsp6H0X073bEYg4TNBdnBF2guMhZCw6wu0BU8j5dp5Rb3nyVDaG82z.KpyWZT750VMGJXnh
============================================================

## Zoom Recording Transcript

**Janhvi** 04:52 Hey, hi Yoshi.
**Yoshi Yamaguchi** 04:55 Happy New Year.
**Janhvi** 04:56 Hey, Happy New Year, can you hear me?
**Yoshi Yamaguchi** 04:59 Yes, I can hear you well.
**Janhvi** 05:01 Okay, okay, I think some issue at my end in the Wi-Fi. How are you doing?
**Yoshi Yamaguchi** 05:06 I'm doing great. I had a relaxed time with my family during the winter break.
How about you?
**Janhvi** 05:16 Same, same. I went on a vacation for the last two weeks, traveled here and there in India, just came back a few days back, but yeah, I had a good, fun time.
**Yoshi Yamaguchi** 05:25 Nice, nice.
Cool, cool.
**Janhvi** 05:30 I don't know if anybody else will be joining the call. Should we get started?
**Yoshi Yamaguchi** 05:36 Why not?
Why not? Yeah.
**Janhvi** 05:39 By the way, does this time work for you?
**Yoshi Yamaguchi** 05:43 Yeah, this time is perfect for me. It's, it's 2.30 PM here, so the best time.
Yeah, yeah.
**Janhvi** 05:51 Yeah, even here, it's 11AM, and it works fine for me. I usually don't have any meetings during this lot.
**Yoshi Yamaguchi** 05:58 Awesome.
**Janhvi** 06:00 Cool. I'll share my screen.
I hope you can see the screen, right?
**Yoshi Yamaguchi** 06:13 Yeah, I do. Can you, can you zoom me in a little bit? Like, can you make the person, the zooming possibilities to, 150? Yeah, that, that works well.
**Janhvi** 06:23 Okay, okay, sounds good. Yeah.
**Yoshi Yamaguchi** 06:25 Yeah, yeah.
**Janhvi** 06:26 Okay, I think, maybe since we didn't meet last time, we can first go through what we had discussed in the other slot. I can give you a quick overview of that, and then we can see if there are more things to discuss on the agenda. Does that make sense?
**Yoshi Yamaguchi** 06:42 Yeah, makes sense. That sounds good.
**Janhvi** 06:44 Okay, okay, sounds good. So, December 4th is when I met, the US folks, last time. After that, even they went on vacation, so we didn't have, any meetings. The next meeting with them is going to have next week, so this is the first meeting for this year that we are having.
Broadly, I think we discussed about criticality. I don't know if you've gotten a chance to look at this PR or not. If not, please do take a look at it. Okay, you did.
**Yoshi Yamaguchi** 07:12 Yeah, I did it, and I did it, and I, I agree with the opinion to put the criticality under… directly under the service, because it's a kind of logical… so the criticality itself is the logical…
like…
it's tied to the logical component, so it should… it doesn't… I believe it doesn't fit to,
service.instances, because instances is just a female, part of, the service. So, yeah, so I, I, I, I think I should… we should put, a critical directory under the service.
**Janhvi** 07:54 Yeah, I agree too. This is what we also discussed, that this makes sense, to have it in this namespace, and it goes with that logical overall, component, not just one specific instance or live running instance of that service or resource.
I'm just taking a quick look at the PR to see where we are at.
**Yoshi Yamaguchi** 08:15 Yeah, I think, as far as I read the PL, so the request, there, the request made here is to eliminate the unnecessary content that is not relevant to the… this issue itself, so…
**Janhvi** 08:30 Yeah.
**Yoshi Yamaguchi** 08:31 And then that is… yeah, and then the review is blocked because of the vacation season, so… yeah.
**Janhvi** 08:37 Makes sense. I think I'll, ping Bhaktia again, who's the author of the CL on Slack. I think most probably they'd be out because of the vacations. If they're back, I'll ask them to see if they can kind of resolve the comments, and we can take it from there. I think one more thing that we did was…
So if you see, Ayushi, she's from Google itself, she works with me. I think Josh and Trask had asked to go through
all the other open source stuff and see if criticality is being used anywhere, what is the naming convention like, what is the usage like, what all definitions are there. So I think she came up with, like, a document for that, just so that we can kind of compare it with other, let's say if it's there in Kubernetes, or any other component, we can just compare it with Hotel and see if what we are doing kind of aligns with that or not.
So, I think in general, criticality… I don't think we were able to find any references in Kubernetes, though, but in general, other than that, there were references in other vendors where criticality is being used, and there are definitive use cases that people have built on criticality. So, definitely makes sense to add criticality there.
In terms of naming conventions and definitions, I think we can debate if we want the wording to be a bit different. I think every vendor or every downstream service or cloud has their own thing.
But on a use case basis, I think the TLDR from the doc that she's added here was that this makes sense to have it in hotel as well.
**Yoshi Yamaguchi** 10:04 Yeah, I agree. As far as I know, the…
Kubernetes only has the priority to the service, and that is not the… that does not directly express the criticality of the service itself, so I don't know if they have…
Similar attributes inside a, like, definition of the services, or deployment, or, like, parts, and so on.
But, yeah, I agree upon the direction to collect the similar terminologies from other services or products.
**Janhvi** 10:37 Yeah, yeah. Yeah, I mean, Kubernetes even, we couldn't find anything. We did a lot of research, so we left it there.
But yeah, yeah, do take a look at the POC doc as well, if you want to just see how is it being used in other places. It's attached in one of the comments in here.
Alright, okay. So I think an AI on me, I'll ping Waktar and see if we can get this resolved. I think once this is done, then we'll have to see… I see there's already a demo for this in this PR.
I'm not sure, then, what is… By the way, would you know what is the process of then stabilizing it? Is it, like, a time duration we have to wait for, or is it just getting more prototypes, for this?
**Yoshi Yamaguchi** 11:23 I'm looking at the… The PR, and then…
I think the demo is closed.
**Janhvi** 11:46 Yeah, I think he had created…
**Yoshi Yamaguchi** 11:50 Yeah, he created it, but because the discussion had stared for a while, it was closed.
Automatically by the… by the bot, so we need to reopen the…
**Janhvi** 11:59 reopen it.
**Yoshi Yamaguchi** 12:00 Reopen it, yeah.
**Janhvi** 12:02 Yeah, yeah, got it.
**Yoshi Yamaguchi** 12:04 Yeah, but, yeah, this, yeah, this sounds great. I, I just took a look at the, the, the DR, and then…
Yeah.
This is really… on fire.
**Janhvi** 12:17 Would you, I'll also… yeah, I'll also review and approve the PR. If you are good with it, can you also go ahead and please approve it? I think that'll also show that from the SIG, we have alignment.
I'll just take an AI for both of us to review and approve the PR if you guys… before, obviously, I'll ask Bhaktia to reopen it, but if you guys are good, we can go ahead and approve it.
**Yoshi Yamaguchi** 12:42 Hmm.
**Janhvi** 12:52 Okay.
All right. Yeah, I think, what I was asking Yoshi, was once this is, let's say, added, right? So this is in development phase right now, the next step would be to kind of, stabilize it. Do you know what is the standard process? We'll need more prototypes on this one, right?
**Yoshi Yamaguchi** 13:12 Yeah. Yeah, I believe so.
**Janhvi** 13:14 Okay, so I think we can do one prototype from Google's site. I know Bhaktar already, the author of the sale, he already has one, prototype. Is there, like, a number that, in general, we target in hotel? Like, how many prototypes are required?
**Yoshi Yamaguchi** 13:33 Actually, I'm not sure how many prototypes are required to get the PRs to be speed stabilized.
**Janhvi** 13:43 Okay, I can check with Josh to see if 2 is enough. If not, we'll probably need more on this one then.
**Yoshi Yamaguchi** 13:52 You know…
**Janhvi** 13:54 And is there, like, a time window that, we usually wait for?
To see how is it being used before taking it into the stable mode.
**Yoshi Yamaguchi** 14:06 Well, the, so… As far as I know, the… the… the status change…
is made by the, who, the tech… the lead, the governor… not the governance committee, but,
I forgot the name of the role, but some role has the rights to, yeah, privilege to change the status, so… as long as we don't get the approval from that person, then we don't get the stability key.
**Janhvi** 14:40 Okay, okay, sounds.
**Yoshi Yamaguchi** 14:41 Yeah.
**Janhvi** 14:42 I'll check.
**Yoshi Yamaguchi** 14:43 Josh should, yeah, Josh should know, yeah, Josh should know.
**Janhvi** 14:45 Perfect, okay, sounds good.
All right, anything else? Any thoughts, comments on the criticality one? If not, we can move on to the next one.
**Yoshi Yamaguchi** 14:55 No, I totally agree with the direction.
**Janhvi** 14:59 Okay.
Next we were… we had discussed about, service.namespace. So, if you remember, Josh had a PR earlier to kind of change the definitions and some naming for the service.namespace and service.instance.id. That PR, got merged earlier, and then I think last time we discussed how do we…
stabilize the rest of the stuff, in service, entity. One was service.instance.id, and the other was service.namespace.
So the direction from both, Josh and Chask was, given there is no pushback in general, and this is, like, something that's widely used.
Let's just go ahead and raise PRs for both of them to stabilize them. We'll keep that open for some time, we'll see how folks feel. If there is no genuine pushback, we can go ahead and stabilize both of them. And if there is a pushback, we'll hear it on the comments itself. So for that, for both of them, so Anav, he's again, he's, he works with me, he's from Google.
He's raised two PRs. I don't know if he's sent them on Slack or not. Let me just add them in here so that you can also…
Take a quick look, just give me a sec.
**Yoshi Yamaguchi** 16:15 Yeah, I haven't… I haven't looked at the PL that are made for that.
**Janhvi** 16:22 Yeah, let me just put them here.
Again, I should have it.
**Yoshi Yamaguchi** 16:33 Okay. Yeah, I see, I see, I see the PR made by, made by Josh.
That was posted on, on, December 2nd, I guess?
**Janhvi** 16:50 I think that one is… is that merged, or that still open?
**Yoshi Yamaguchi** 16:54 That was merged.
**Janhvi** 16:56 Yo.
So, I think these are the two PRs that were raised, I think, after that, and I've raised them.
Both of them are stabilizing the, attributes under service. Okay. Service.instance and service.namespace.
This is one. I've added both of them, in the notes doc.
These are, like, both simple PRs. I got an example… Trask had sent an example of how you usually make a PR stable in hotel. Here are two examples, we just followed that same thing.
We specifically, we've not added any prototypes or, other docs to it, because this is something that's been widely used, and we've heavily discussed this already. So yeah, we're just trying to see if there are comments, questions from anybody in the PR, and then we can kind of add that data.
When we get that on the comments. But I wanted to hear from you if you have any thoughts around this. I know you've not taken a look at it, and that's fine, we can discuss it later also, but if any early thoughts do, let me know.
**Yoshi Yamaguchi** 18:17 Yeah, I just… I just took a glance of these, PRs, and then, the changes on these POs, and then it looks good to me, so… yeah.
**Janhvi** 18:25 I have no objection on that.
Sounds good. Yeah, please do review them offline whenever you get time. I'll also review the last to post this on the Slack channel, so that it gets more traction, in the SIG channel that we have on Slack.
I think more people would be able to see it from there.
**Yoshi Yamaguchi** 18:45 Is it okay for me to, like, make a comment on draft PRs?
Or do I, do I, do I… should I, should I wait for… the…
Like, for it to be, like.
**Janhvi** 18:58 No, no, it's okay. I think this is the first time he was doing it. I'll ask him to create, like, a formal PR on the same thing, but go ahead, please add any feedback that you have.
**Yoshi Yamaguchi** 19:09 Okay.
**Janhvi** 19:11 Sweet.
Okay, and the final thing that we discussed was around deployment.environment.name.
We were discussing, so even, this is, again, one of the attributes that we want to stabilize as part of this SIG, right?
and we were trying to see how do we stabilize this. As of now, this is in a development mode, but environment is something that is heavily used across clouds and, across downstreams like Rifana, Datadog, stuff like that. So, I think it makes sense to stabilize it.
But what, we're trying to see is if we can come up with, like, a one-pager where we write down all the usages of deployment.environment.name, how is it being used, let's say, in Cuban, it is the same thing that we did for criticality, basically. Follow the same process, have a doc, look into usages.
And then form up a proposal on how we stabilize it. That's the AI we have. I have that, I've not done it, but hopefully in a day or two, I should have that proposal, and I'll send it out for review. And then we'll follow the same process here.
**Yoshi Yamaguchi** 20:26 Should we reach out to the… the folks,
in, like, deployment service software communities, such as IowaCD or, like, speedmakers, or any other…
these type of… Like, these type of services that are directly
Connected to a deployment process itself.
like a CICD.
**Janhvi** 20:57 Yeah.
**Yoshi Yamaguchi** 20:58 community people.
**Janhvi** 21:01 I see. Just to hear feedback from them on how they use it, and the way we've modeled in OTEL, is that the right way of modeling it? Around that, are you saying?
**Yoshi Yamaguchi** 21:12 Yeah, so the reason why I ask this is because the Kubernetes or other runtime services are just the result of the deployment, and then…
I… I'm sure… I'm not sure if…
Kubernetes or other runtime services are aware of these type of standardization much.
So, and then DevOps people are always about… they are always talking about deployment, a lot. Like, CICD, and then…
Yeah, it would be great if he can…
Get the insights from those, kind of.
**Janhvi** 21:49 Bye.
**Yoshi Yamaguchi** 21:52 From people who are… Focusing on the process of deployment.
**Janhvi** 21:57 Hmm.
basically the DevOps side of things, who usually.
**Yoshi Yamaguchi** 22:02 Yeah, yeah, yeah. Yeah, yeah, yeah.
**Janhvi** 22:04 Yeah.
**Yoshi Yamaguchi** 22:05 Under CNCF, we have Argo City athletes, so, Argo City people should know better.
About these kind of topics.
**Janhvi** 22:16 I see. Would you, by any chance, have, like, contacts of them? Who should we reach out to? Who should be the first point of contact?
**Yoshi Yamaguchi** 22:24 Yes. Well, the problem here is that, as you are aware of, except for Kubernetes, we don't have much contributors to the, the project themselves, like.
**Janhvi** 22:36 Hmm.
**Yoshi Yamaguchi** 22:37 So we… so most of the Japanese developers are just the use…
just users of these OSS. So, yeah, so I know some folks who are really, who are really good at
using… Those kind of.
**Janhvi** 22:53 Yeah.
**Yoshi Yamaguchi** 22:53 you know, CICD drug OSS, but they're not contributors, so…
Yeah, I can reach out to them, but I'm not sure if that kind of…
That kind of opinions are well considered.
In the discussion or not.
**Janhvi** 23:12 Yeah, yeah, no, I agree. Even I don't think I know… I mean, I know the consumers of it, though, but I don't know, again, if we get a lot of help from them.
I mean, I know at least, on our end in GCP, right? So, the team that I work in, it's like a platform team, and the product manager here, they reached out to, like, a couple of,
end users who actually use GCP in their whole organizations, right? There are a couple of clients who use it. So we know how they use environment, and how they build automation on top of environment, so that they can view their resources. Let's say, they can view, dashboards saying, hey, give me all the resources which have production tag associated with it.
Right? They do all of that stuff today manually, but again, they're like the consumers, end users of it, right? They're not the ones who are deploying stuff.
So, yeah, again, I can also see if I have somebody, but I don't know if we'll be… if I'll be able to get the right POCs for this.
**Yoshi Yamaguchi** 24:17 So,
Well, I have… so if… I'm not sure if this helps, but I have conducted the personal survey to the… to the community… community about a deployment environment name.
And then…
So this is the result. I think you have the access. Though… though it's all written, like, the columns are written in Japanese, you can tell the labels used for the deployment name, environment name, so if it helps, yeah, that'd be great.
**Janhvi** 24:52 Oh, this actually helps. And this tells you that we are on the right track. Like, if you see, right, most of them are production, development, staging.
**Yoshi Yamaguchi** 25:01 Yeah, yeah.
**Janhvi** 25:02 Yeah… Okay, so this is a survey that you conducted.
**Yoshi Yamaguchi** 25:09 Yeah, yeah, I, I conducted throughout the, yeah, my, my, my, my timeline.
I see. Let me, yeah, let, the, the original…
form for this is, how can I get the form? Blink of form.
I think this is the one.
No, not this… not this one.
How can… so do you have the, Google account?
which I can share the link to the form.
**Janhvi** 25:54 Yeah, yeah, can you just share it on my, the…
**Yoshi Yamaguchi** 25:58 I think you have, you have the link, or you have the, access. So… Very sick.
**Janhvi** 26:17 Yeah, I think I should've…
**Yoshi Yamaguchi** 26:19 Can you open?
**Janhvi** 26:20 No.
It opens the responses, not the.
**Yoshi Yamaguchi** 26:23 Okay, well, let me, let me see. I think it's, yeah, you've added the same. Oh, okay. Okay, okay, yeah.
Link.
And then…
**Janhvi** 26:45 Thank you.
**Yoshi Yamaguchi** 26:45 Change the link.
**Janhvi** 26:47 I see, let me… Oh yeah, I can see it now. Okay.
**Yoshi Yamaguchi** 26:52 So, I…
**Janhvi** 26:54 So I…
**Yoshi Yamaguchi** 26:55 picked a couple of famous, production names, environment names, but I asked the… the…
Other possible name for the environment.
**Janhvi** 27:08 I see.
**Yoshi Yamaguchi** 27:09 Oh, yep.
**Janhvi** 27:11 Got it. And there's a…
**Yoshi Yamaguchi** 27:13 issue here for this? Is this referring to a similar…
Yeah, I think this is the original… Discussion we made.
**Janhvi** 27:24 I see. Should this be an enum or not? Okay, got it.
**Yoshi Yamaguchi** 27:28 Yeah, yeah, yeah.
**Janhvi** 27:32 Okay.
**Yoshi Yamaguchi** 27:34 Yeah.
**Janhvi** 27:37 How should we, like, what was the final conclusion on this one?
**Yoshi Yamaguchi** 27:44 There is no conclusion here.
**Janhvi** 27:46 Hmm.
Got it.
And I think, this person, Thompson, right, are they, like, from CICD sometime?
**Yoshi Yamaguchi** 28:01 Maybe.
**Janhvi** 28:03 Okay.
So at least they're bringing that POV that we were discussing, right?
Yeah, okay.
Yeah, I mean, I… in general, I think I'm aligned with the fact that it could be, like, an open enum, where you at least give them 3 to 4 well-known properties, like development.
**Yoshi Yamaguchi** 28:24 Productions here.
**Janhvi** 28:25 And then…
I don't know, in Hotel, can you do, like, a fourth place to say others, where you can have freeform text also? Like, three we've already defined, and if somebody wants to use more values, they can do that. That should be possible, right?
**Yoshi Yamaguchi** 28:41 Yeah.
**Janhvi** 28:43 Yeah, so I think I am… Lind, yeah.
**Yoshi Yamaguchi** 28:45 In order to reduce the, reduce the… the cardinality.
**Janhvi** 28:51 Yup.
**Yoshi Yamaguchi** 28:52 My personal opinion is to provide the, like.
**Janhvi** 28:58 Provide the… the options to cover 90% of the use case.
**Yoshi Yamaguchi** 29:03 And then for the list of the 10%, we can… still, they can use the… others… Or other…
**Janhvi** 29:12 Hog, and then…
**Yoshi Yamaguchi** 29:13 Put their own… I, I, or I… we can, we can, we can provide the, recommended
Name of the labels.
**Janhvi** 29:24 Got it.
**Yoshi Yamaguchi** 29:24 The attribute for, for, for the, for the, for the… the label.
**Janhvi** 29:30 Because.
**Yoshi Yamaguchi** 29:31 Yeah, buddy, body, yeah.
**Janhvi** 29:33 Yeah, because then you're catering for majority of the use cases, right? And anybody who's, let's say, new.
who's coming to it and seeing the standard for the first time, they kind of know what is already recommended by the society, by the open source community, right? And they kind of choose from there. If you don't give them anything, then even if they want production, they may use it as prod, production, or something else, even though they mean the same thing. So at least you give them some standard that they can use from, and that kind of handles majority of your use cases.
That's true and true.
Yeah.
**Yoshi Yamaguchi** 30:09 Yeah, and also if we… yeah, and also, if we provide the, the standard option for them, then we can…
Could… we can…
offer the extra, like, linter or formatter to, to… or validation tools to find if they're using in recommended.
**Janhvi** 30:32 The value for the, for the label.
**Yoshi Yamaguchi** 30:35 Or not later, anyway. So, yeah, at least we should provide us a couple of recommendations
For the… for the environment name, and then…
**Janhvi** 30:47 Yeah.
**Yoshi Yamaguchi** 30:48 And then we can discuss about, like, putting those labels, all mandatory or not.
**Janhvi** 30:54 Yeah, yeah, I totally agree.
Makes sense. Okay, I think next thing, then, let me do is, let me at least come up with that proposal for deployment.
I'll socialize it, I'll try to send it by this week, and end of this week, either tomorrow or day after. And then next week, we guys can go through it.
And then we can discuss debate on top of it, how we want to take this to stabilization, and I'll also, kind of, next week, when I meet the rest of the folks, right, I'll nudge them for the PR that Hao had raised on the enum thing, and I'll try to see how we can bring that to closure.
**Yoshi Yamaguchi** 31:31 Sounds good.
**Janhvi** 31:32 Okay, cool.
I'll take an AI for me on this one.
Alright.
What else? I don't have anything else to discuss. I think these are the ones that we've been discussing for now. Anything from your end, Yoshi?
**Yoshi Yamaguchi** 32:06 Not much.
**Janhvi** 32:08 Okay, cool. Let's at least then, I think we have a few AIs on the both of us reviewing the already, raised PRs, let's do that, and then I'll send the proposal from my end.
**Yoshi Yamaguchi** 32:21 Awesome.
**Janhvi** 32:21 Okay, cool, sounds good. Thank you.
**Yoshi Yamaguchi** 32:25 Yeah, thank you, John V.
**Janhvi** 32:26 Thanks, bye. Have a good day.
**Yoshi Yamaguchi** 32:28 Bye, you too.
